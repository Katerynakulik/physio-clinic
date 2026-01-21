from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone

from .models import BookingSlot
from .utils import ensure_slots_for_physio


@login_required
def physio_schedule(request):
    """
    Physiotherapist schedule view: shows all slots (available/booked/blocked).
    Blocked slots show a reason. Booked slots show client + note.
    """
    if not hasattr(request.user, "physiotherapist"):
        return HttpResponseForbidden("Access denied")

    physio = request.user.physiotherapist
    ensure_slots_for_physio(physio, days_ahead=21)

    slots = BookingSlot.objects.filter(
        physiotherapist=physio,
        date__gte=timezone.now().date(),
    ).order_by("date", "start_time")

    return render(request, "bookings/physio_schedule.html", {"slots": slots})


@login_required
def block_slot(request, slot_id):
    """
    Block an available slot (POST only). Blocked slots are hidden from clients.
    """
    if request.method != "POST":
        return redirect("physio_schedule")

    if not hasattr(request.user, "physiotherapist"):
        return HttpResponseForbidden("Access denied")

    physio = request.user.physiotherapist

    slot = get_object_or_404(BookingSlot, id=slot_id, physiotherapist=physio)

    # Only allow blocking if slot is not booked
    if slot.status == BookingSlot.STATUS_BOOKED:
        return redirect("physio_schedule")

    reason = (request.POST.get("blocked_reason") or "").strip()

    slot.status = BookingSlot.STATUS_BLOCKED
    slot.blocked_reason = reason
    slot.client = None
    slot.client_note = ""
    slot.save()

    return redirect("physio_schedule")
