from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.utils import timezone

from .models import BookingSlot
from .utils import ensure_slots_for_physio
from .forms import BookingSlotForm


def is_physio(user):
    """
    Helper function to check if the user has a physiotherapist profile.
    Used by user_passes_test decorator.
    """
    return hasattr(user, 'physiotherapist')


@login_required
@user_passes_test(is_physio)
def physio_schedule(request):
    """
    Display the physiotherapist's schedule.
    Automatically triggers slot generation via ensure_slots_for_physio.
    """
    physio = request.user.physiotherapist
    # Automated logic: ensures default slots exist for the next 21 days
    ensure_slots_for_physio(physio, days_ahead=21)

    slots = BookingSlot.objects.filter(
        physiotherapist=physio,
        date__gte=timezone.now().date(),
    ).order_by("date", "start_time")

    return render(request, "bookings/physio_schedule.html", {"slots": slots})


@login_required
@user_passes_test(is_physio)
def create_slot(request):
    """
    Manually create a single booking slot (CRUD: Create).
    """
    physio = request.user.physiotherapist
    if request.method == "POST":
        # ПЕРЕДАЄМО фізіотерапевта у форму
        form = BookingSlotForm(request.POST, physiotherapist=physio)
        if form.is_valid():
            slot = form.save(commit=False)
            slot.physiotherapist = physio
            slot.save()
            messages.success(request, "New slot created successfully!")
            return redirect("physio_schedule")
    else:
        # ПЕРЕДАЄМО фізіотерапевта у форму навіть для порожньої форми
        form = BookingSlotForm(physiotherapist=physio)
    
    return render(
        request, 
        "bookings/slot_form.html", 
        {"form": form, "title": "Create Slot"}
    )


@login_required
@user_passes_test(is_physio)
def block_slot(request, slot_id):
    """
    Block an existing slot to make it unavailable for clients (CRUD: Update).
    """
    if request.method != "POST":
        return redirect("physio_schedule")

    physio = request.user.physiotherapist
    slot = get_object_or_404(BookingSlot, id=slot_id, physiotherapist=physio)

    if slot.status == BookingSlot.STATUS_BOOKED:
        messages.error(request, "Cannot block a slot that is already booked.")
        return redirect("physio_schedule")

    reason = (request.POST.get("blocked_reason") or "").strip()
    slot.status = BookingSlot.STATUS_BLOCKED
    slot.blocked_reason = reason
    slot.save()
    
    messages.info(request, "Slot status updated to Blocked.")
    return redirect("physio_schedule")


@login_required
@user_passes_test(is_physio)
def delete_slot(request, slot_id):
    """
    Permanently delete a slot from the database (CRUD: Delete).
    This function is essential to meet the project's CRUD requirements.
    """
    physio = request.user.physiotherapist
    slot = get_object_or_404(BookingSlot, id=slot_id, physiotherapist=physio)
    
    # Security check: prevent deletion of active bookings
    if slot.status == BookingSlot.STATUS_BOOKED:
        messages.error(request, "Cannot delete a slot that is already booked.")
        return redirect("physio_schedule")

    if request.method == "POST":
        slot.delete()
        messages.success(request, "Slot has been permanently deleted.")
        return redirect("physio_schedule")
    
    return render(
        request, 
        "bookings/slot_confirm_delete.html", 
        {"slot": slot}
    )


@login_required
@user_passes_test(is_physio)
def cancel_booking_physio(request, slot_id):
    """
    Allows a physiotherapist to cancel a client's booking.
    Resets the slot status back to 'Available'.
    """
    if request.method != "POST":
        return redirect("physio_dashboard")

    physio = request.user.physiotherapist
    slot = get_object_or_404(
        BookingSlot,
        id=slot_id,
        physiotherapist=physio,
        status=BookingSlot.STATUS_BOOKED,
    )

    # Validation: prevent canceling past appointments
    now = timezone.localtime()
    if slot.date < now.date() or (slot.date == now.date() and slot.start_time <= now.time()):
        messages.warning(request, "Cannot cancel appointments in the past.")
        return redirect("physio_dashboard")

    slot.status = BookingSlot.STATUS_AVAILABLE
    slot.client = None
    slot.client_note = ""
    slot.save()

    messages.success(request, "Booking cancelled successfully. Slot is now available.")
    return redirect("physio_dashboard")