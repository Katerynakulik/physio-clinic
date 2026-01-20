from django.db import models
from django.conf import settings
from accounts.models import Physiotherapist


class BookingSlot(models.Model):
    """
    Represents a single bookable time slot
    for a physiotherapist.
    """

    physiotherapist = models.ForeignKey(
        Physiotherapist,
        on_delete=models.CASCADE,
        related_name="slots"
    )

    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_booked = models.BooleanField(default=False)

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings"
    )

    class Meta:
        ordering = ["date", "start_time"]
        unique_together = ("physiotherapist", "date", "start_time")

    def __str__(self):
        return f"{self.physiotherapist} | {self.date} {self.start_time}"
