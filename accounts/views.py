"""
Views for handling user authentication, registration, and role-based dashboards.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.utils import timezone
from django.contrib import messages
from .forms import ClientRegistrationForm
from .models import ClientProfile
from bookings.models import BookingSlot


def register_client(request):
    """
    Handles new client registration.
    Creates a User and an associated ClientProfile upon successful form submission.
    """
    if request.method == "POST":
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClientProfile.objects.create(user=user)
            login(request, user)
            messages.success(
                request, f"Welcome to our clinic, {user.first_name}!")
            return redirect("client_dashboard")
    else:
        form = ClientRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


@login_required
def client_dashboard(request):
    """
    Displays the personal dashboard for clients, showing their upcoming appointments.
    Restricts access to users without a ClientProfile.
    """
    if not hasattr(request.user, "clientprofile"):
        return HttpResponseForbidden("Access denied")

    upcoming = BookingSlot.objects.filter(
        client=request.user,
        status=BookingSlot.STATUS_BOOKED,
        date__gte=timezone.now().date(),
    ).order_by("date", "start_time")

    return render(request, "accounts/client_dashboard.html", {"upcoming": upcoming})


@login_required
def physio_dashboard(request):
    """
    Displays the professional dashboard for physiotherapists.
    Shows all slots (available, booked, blocked) for the logged-in specialist.
    """
    if not hasattr(request.user, "physiotherapist"):
        return HttpResponseForbidden("Access denied")

    physio = request.user.physiotherapist
    slots = BookingSlot.objects.filter(
        physiotherapist=physio,
        date__gte=timezone.localdate(),
    ).order_by("date", "start_time")

    return render(request, "accounts/physio_dashboard.html", {"slots": slots})


class RoleBasedLoginView(LoginView):
    """
    Extends Django's LoginView to provide dynamic redirection.
    Sends users to different dashboards depending on their profile type (Physio vs Client).
    """
    template_name = "accounts/login.html"

    def get_success_url(self):
        """Determines the dashboard URL based on the user's related profile."""
        user = self.request.user
        if hasattr(user, "clientprofile"):
            return "/accounts/client/dashboard/"
        if hasattr(user, "physiotherapist"):
            return "/accounts/physio/dashboard/"
        return "/"
