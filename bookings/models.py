from django.db import models
from accounts.models import ClientProfile, Physiotherapist

class Booking(models.Model):
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    physiotherapist = models.ForeignKey(Physiotherapist, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client} - {self.date} {self.time}"
