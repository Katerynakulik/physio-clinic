from datetime import datetime, time, timedelta

from .models import BookingSlot


def ensure_slots_for_physio(physio, days_ahead=21):
    """
    Ensure hourly slots exist for each weekday for the next N days.
    Default working hours: 09:00–18:00 (end exclusive).
    Slots are created only if missing (idempotent).
    """

    today = datetime.today().date()

    work_start = getattr(physio, "working_from", None) or time(9, 0)
    work_end = getattr(physio, "working_to", None) or time(18, 0)

    for day_offset in range(days_ahead + 1):
        slot_date = today + timedelta(days=day_offset)

        # Weekdays only: Monday(0) ... Friday(4)
        if slot_date.weekday() > 4:
            continue

        current = datetime.combine(slot_date, work_start)
        end_dt = datetime.combine(slot_date, work_end)

        while current < end_dt:
            next_dt = current + timedelta(hours=1)

            BookingSlot.objects.get_or_create(
                physiotherapist=physio,
                date=slot_date,
                start_time=current.time(),
                end_time=next_dt.time(),
                defaults={"status": BookingSlot.STATUS_AVAILABLE},
            )

            current = next_dt
