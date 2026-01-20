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
    working_from = models.TimeField()
    working_to = models.TimeField()

    def __str__(self):
        return self.user.get_full_name()