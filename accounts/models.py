"""
Models for the accounts app.
Defines user profiles for Clients and Physiotherapists using
OneToOne relationships with the Django built-in User model.
"""
from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    """
    Extends the base User model with specific data for clinic patients.

    Attributes:
        user (OneToOneField): Link to the Django User model.
        phone (CharField): Contact phone number.
        insurance_number (CharField): Medical insurance identifier.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    insurance_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.email


class Physiotherapist(models.Model):
    """
    Represents a medical professional in the system.
    Stores professional details, availability hours, and profile photos.

    Attributes:
        specialization (CharField): Professional focus area.
        photo_static_path (CharField): Reliable path for static images on
        Heroku.
        working_from/to (TimeField): Daily shift boundaries.
        last_generated_until (DateField): Tracks the timeline of
        pre-generated slots.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="physiotherapists/", blank=True, null=True)
    photo_static_path = models.CharField(max_length=255, blank=True)

    working_from = models.TimeField()
    working_to = models.TimeField()
    last_generated_until = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.get_full_name()
