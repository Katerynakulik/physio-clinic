"""
Business logic layer for calculating time slot availability.
Separates data processing from views to maintain a clean architecture.
"""
from datetime import time, timedelta, datetime
from .models import Booking, BlockedSlot


def generate_daily_slots():
    """
    Returns a list of hourly time objects within standard clinic hours (9-18).
    """
    start = time(9, 0)
    end = time(18, 0)

    slots = []
    current = datetime.combine(datetime.today(), start)

    while current.time() < end:
        slots.append(current.time())
        current += timedelta(hours=1)

    return slots


def get_available_slots(physiotherapist, date):
    """
    Calculates a list of free time slots by excluding already booked
    or manually blocked appointments for a specific date.
    """
    all_slots = generate_daily_slots()

    booked = Booking.objects.filter(
        physiotherapist=physiotherapist,
        date=date,
        is_cancelled=False
    ).values_list('time', flat=True)

    blocked = BlockedSlot.objects.filter(
        physiotherapist=physiotherapist,
        date=date
    ).values_list('time', flat=True)

    return [
        slot for slot in all_slots
        if slot not in booked and slot not in blocked
    ]
