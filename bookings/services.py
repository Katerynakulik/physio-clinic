from datetime import time, timedelta, datetime
from .models import Booking, BlockedSlot

# Slot availability service

def generate_daily_slots():
    start = time(9, 0)
    end = time(18, 0)

    slots = []
    current = datetime.combine(datetime.today(), start)

    while current.time() < end:
        slots.append(current.time())
        current += timedelta(hours=1)

    return slots


def get_available_slots(physiotherapist, date):
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
