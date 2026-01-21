from django.db import models
from django.contrib.auth.models import User

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    insurance_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.email


class Physiotherapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    short_description = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    working_from = models.TimeField()
    working_to = models.TimeField()

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()
