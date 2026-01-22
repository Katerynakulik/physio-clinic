from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden

from .forms import ClientRegistrationForm
from .models import ClientProfile

from django.utils import timezone
from bookings.models import BookingSlot





def register_client(request):
    """
    Register a new client user and redirect
    to client dashboard after successful signup.
    """
    if request.method == "POST":
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ClientProfile.objects.create(user=user)
            login(request, user)
            return redirect("client_dashboard")
    else:
        form = ClientRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})



@login_required
def client_dashboard(request):
    """
    Dashboard page for logged-in clients.
    Shows future booked appointments.
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
    Dashboard page for physiotherapists.
    Accessible only for users with Physiotherapist profile.
    """
    if not hasattr(request.user, "physiotherapist"):
        return HttpResponseForbidden("Access denied")
    physio = request.user.physiotherapist
    slots = BookingSlot.objects.filter(
        physiotherapist=physio,
        date__gte=timezone.localdate(),
    ).order_by("date", "start_time")

    return render(
        request,
        "accounts/physio_dashboard.html",
        {"slots": slots}, 
    )
class RoleBasedLoginView(LoginView):
    """
    Custom login view that redirects users
    based on related profile existence.
    """

    template_name = "accounts/login.html"

    def get_success_url(self):
        """
        Determine redirect destination after login
        depending on user type.
        """
        user = self.request.user

        # Client users
        if hasattr(user, "clientprofile"):
            return "/accounts/client/dashboard/"

        # Physiotherapist users
        if hasattr(user, "physiotherapist"):
            return "/accounts/physio/dashboard/"

        # Safety fallback
        return "/"
