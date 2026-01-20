from datetime import time, timedelta, datetime
from .models import BookingSlot


def generate_daily_slots(physiotherapist, date):
    """
    Generate hourly booking slots for a given physiotherapist
    on a specific date (09:00–18:00).
    """

    start_hour = 9
    end_hour = 18

    current_time = time(start_hour, 0)

    while current_time.hour < end_hour:
        end_time = (datetime.combine(date, current_time)
                    + timedelta(hours=1)).time()

        BookingSlot.objects.get_or_create(
            physiotherapist=physiotherapist,
            date=date,
            start_time=current_time,
            end_time=end_time
        )

        current_time = end_time
