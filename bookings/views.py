from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone

from accounts.models import Physiotherapist
from .models import BookingSlot
from .utils import ensure_slots_for_physio


@login_required
def booking_home(request):
    """
    Show a list of physiotherapists to start a booking.
    """
    physiotherapists = Physiotherapist.objects.filter(is_active=True) if hasattr(Physiotherapist, "is_active") else Physiotherapist.objects.all()
    return render(request, "bookings/booking_home.html", {"physiotherapists": physiotherapists})


@login_required
def booking_page(request, physio_id):
    """
    Display available booking slots for a selected physiotherapist.
    Auto-generates missing slots for upcoming weekdays.
    """
    physiotherapist = get_object_or_404(Physiotherapist, id=physio_id)

    # Ensure slots exist for upcoming period
    ensure_slots_for_physio(physiotherapist, days_ahead=21)

    # Only available slots should be visible to clients
    slots = BookingSlot.objects.filter(
        physiotherapist=physiotherapist,
        status=BookingSlot.STATUS_AVAILABLE,
        date__gte=timezone.now().date(),
    )

    return render(
        request,
        "bookings/booking_page.html",
        {"physiotherapist": physiotherapist, "slots": slots},
    )


@login_required
def book_slot(request, slot_id):
    """
    Book a specific available slot (POST only).
    Client may provide an optional note.
    """
    if request.method != "POST":
        return redirect("booking_home")

    # Only clients can book
    if not hasattr(request.user, "clientprofile"):
        return HttpResponseForbidden("Access denied")

    slot = get_object_or_404(
        BookingSlot,
        id=slot_id,
        status=BookingSlot.STATUS_AVAILABLE
    )

    client_note = (request.POST.get("client_note") or "").strip()

    slot.status = BookingSlot.STATUS_BOOKED
    slot.client = request.user
    slot.client_note = client_note
    slot.save()

    return redirect("client_dashboard")
