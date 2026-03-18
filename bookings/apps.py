from django.apps import AppConfig

class BookingsConfig(AppConfig):
    """
    Configuration for the Bookings application.
    Sets the default primary key type and names the app for Django registry.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'