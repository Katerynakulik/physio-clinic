from datetime import datetime, timedelta, date
from .models import BookingSlot

def ensure_slots_for_physio(physio, days_ahead=21):
    """
    Automated logic to generate daily booking slots for a physiotherapist.
    It prevents recreated deleted slots by using a 'checkpoint' field.
    """
    today = date.today()
    # Define the date up to which we want to have slots
    target_date = today + timedelta(days=days_ahead)
    
    # Logic to handle persistent deletion:
    # We only start generating from the day after the last successful generation.
    # If it's a new physio, we start from today.
    if physio.last_generated_until:
        start_date = physio.last_generated_until + timedelta(days=1)
    else:
        start_date = today
    
    # If we have already generated slots up to or beyond the target, stop here.
    if start_date > target_date:
        return

    current_date = start_date
    while current_date <= target_date:
        # Business logic: generate slots for weekdays only (Monday to Friday)
        # weekday() returns 0 for Monday and 6 for Sunday.
        if current_date.weekday() < 5: 
            # Use the physio's specific working hours from the model
            start_hour = physio.working_from.hour
            end_hour = physio.working_to.hour
            
            # Generate hourly slots based on working hours
            for hour in range(start_hour, end_hour):
                start_t = datetime.strptime(f"{hour}:00", "%H:%M").time()
                end_t = datetime.strptime(f"{hour+1}:00", "%H:%M").time()
                
                # get_or_create is used as a safety measure against manual duplicates
                BookingSlot.objects.get_or_create(
                    physiotherapist=physio,
                    date=current_date,
                    start_time=start_t,
                    end_time=end_t,
                    defaults={'status': BookingSlot.STATUS_AVAILABLE}
                )
        
        current_date += timedelta(days=1)
    
    # Update the physio checkpoint so this period isn't processed again
    physio.last_generated_until = target_date
    physio.save()