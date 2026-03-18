"""
Utility functions for the bookings app.
Handles background automation such as slot generation.
"""
from datetime import datetime, timedelta, date
from .models import BookingSlot


def ensure_slots_for_physio(physio, days_ahead=21):
    """
    Automatically generates daily 1-hour booking slots for a physiotherapist.

    Logic:
    1. Checks the 'last_generated_until' checkpoint to avoid re-generating deleted slots.
    2. Iterates through weekdays (Mon-Fri) within the target range.
    3. Uses the physiotherapist's specific working hours to create hourly BookingSlot objects.
    4. Employs get_or_create to prevent IntegrityErrors from manual duplicates.

    Args:
        physio (Physiotherapist): The profile instance to generate slots for.
        days_ahead (int): How many days into the future slots should be created.
    """
    today = date.today()
    target_date = today + timedelta(days=days_ahead)

    if physio.last_generated_until:
        start_date = physio.last_generated_until + timedelta(days=1)
    else:
        start_date = today

    if start_date > target_date:
        return

    current_date = start_date
    while current_date <= target_date:
        # Generate only for weekdays
        if current_date.weekday() < 5:
            start_hour = physio.working_from.hour
            end_hour = physio.working_to.hour

            for hour in range(start_hour, end_hour):
                start_t = datetime.strptime(f"{hour}:00", "%H:%M").time()
                end_t = datetime.strptime(f"{hour+1}:00", "%H:%M").time()

                BookingSlot.objects.get_or_create(
                    physiotherapist=physio,
                    date=current_date,
                    start_time=start_t,
                    end_time=end_t,
                    defaults={'status': BookingSlot.STATUS_AVAILABLE}
                )

        current_date += timedelta(days=1)

    physio.last_generated_until = target_date
    physio.save()
