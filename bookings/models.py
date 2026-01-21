from django.db import models
from django.conf import settings
from accounts.models import Physiotherapist


class BookingSlot(models.Model):
    """
    Represents a single time slot for a physiotherapist.
    A slot can be:
    - available: visible to clients
    - booked: booked by a client, visible to both
    - blocked: blocked by the physiotherapist, hidden from clients
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

    # Client is set only when status == booked
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings"
    )

    # Optional note entered by the client during booking (visible to physio & client)
    client_note = models.TextField(blank=True)

    # Optional reason entered by the physio when blocking the slot (visible to physio only)
    blocked_reason = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ["date", "start_time"]
        unique_together = ("physiotherapist", "date", "start_time")

    def __str__(self):
        return f"{self.physiotherapist} | {self.date} {self.start_time} ({self.status})"
