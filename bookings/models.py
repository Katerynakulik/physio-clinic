"""
Models for the bookings app.
Defines the BookingSlot model which acts as the core entity for the 
appointment system, linking Physiotherapists and Clients.
"""
from django.db import models
from django.conf import settings
from accounts.models import Physiotherapist


class BookingSlot(models.Model):
    """
    Represents an individual time slot for a physiotherapy session.

    Attributes:
        STATUS_CHOICES (list): Defines three states: Available, Booked, and Blocked.
        physiotherapist (ForeignKey): Link to the professional providing the service.
        client (ForeignKey): Link to the User who booked the slot (optional).
        physio_note (CharField): Private notes for the physiotherapist.
        client_note (TextField): Notes provided by the patient during booking.
        blocked_reason (CharField): Reason for manually blocking a slot (e.g., Vacation).
    """

    STATUS_AVAILABLE = "available"
    STATUS_BOOKED = "booked"
    STATUS_BLOCKED = "blocked"

    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Available"),
        (STATUS_BOOKED, "Booked"),
        (STATUS_BLOCKED, "Blocked"),
    ]

    physiotherapist = models.ForeignKey(
        Physiotherapist,
        on_delete=models.CASCADE,
        related_name="slots"
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_AVAILABLE
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings"
    )
    physio_note = models.CharField(max_length=255, blank=True)
    client_note = models.TextField(blank=True)
    blocked_reason = models.CharField(max_length=200, blank=True)

    class Meta:
        """Enforces unique time slots per physiotherapist and default sorting."""
        ordering = ["date", "start_time"]
        unique_together = ("physiotherapist", "date", "start_time")

    def __str__(self):
        return f"{self.physiotherapist} | {self.date} {self.start_time} ({self.status})"
