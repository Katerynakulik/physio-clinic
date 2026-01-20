from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Physiotherapist
from .models import BookingSlot


@login_required
def booking_page(request, physio_id):
    """
    Display available booking slots
    for a selected physiotherapist.
    """

    physiotherapist = get_object_or_404(
        Physiotherapist, id=physio_id
    )

    slots = BookingSlot.objects.filter(
        physiotherapist=physiotherapist,
        is_booked=False
    )

    return render(
        request,
        "bookings/booking_page.html",
        {
            "physiotherapist": physiotherapist,
            "slots": slots
        }
    )


@login_required
def book_slot(request, slot_id):
    """
    Book a specific slot for the logged-in client.
    """

    slot = get_object_or_404(
        BookingSlot,
        id=slot_id,
        is_booked=False
    )

    slot.is_booked = True
    slot.client = request.user
    slot.save()

    return redirect("client_dashboard")
