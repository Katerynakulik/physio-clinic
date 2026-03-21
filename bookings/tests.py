"""
Automated tests for the bookings app.
Tests cover model creation, access control, and core booking logic.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import Physiotherapist, ClientProfile
from .models import BookingSlot
import datetime

# Get the custom user model defined in settings
User = get_user_model()


class BookingSystemTests(TestCase):
    """
    Test suite for the booking system functionality.
    Includes validation of models, security constraints, and defensive design.
    """

    def setUp(self):
        """
        Set up initial test data for all test cases.
        Creates a physiotherapist, a client, and an available time slot.
        """
        # Create users for different roles
        self.physio_user = User.objects.create_user(
            username='physio_user', password='password123')
        self.client_user = User.objects.create_user(
            username='client_user', password='password123')

        # Create corresponding profiles
        # Added working_from and working_to to avoid IntegrityError
        self.physio_profile = Physiotherapist.objects.create(
            user=self.physio_user,
            specialization="Orthopedic",
            working_from=datetime.time(9, 0),
            working_to=datetime.time(17, 0),
            is_active=True
        )
        self.client_profile = ClientProfile.objects.create(
            user=self.client_user)

        # Create a test slot for a future date (tomorrow)
        self.slot = BookingSlot.objects.create(
            physiotherapist=self.physio_profile,
            date=timezone.now().date() + datetime.timedelta(days=1),
            start_time=datetime.time(10, 0),
            end_time=datetime.time(11, 0),
            status='available'
        )

    def test_slot_model_creation(self):
        """
        Verify that the BookingSlot model correctly stores data 
        and returns the expected string representation.
        """
        expected_str = f"{self.physio_profile} | {self.slot.date} 10:00:00 (available)"
        self.assertEqual(str(self.slot), expected_str)

    def test_booking_home_access_logged_in(self):
        """
        Check that an authenticated client can successfully 
        access the physiotherapist list page.
        """
        self.client.login(username='client_user', password='password123')
        response = self.client.get(reverse('booking_home'))
        self.assertEqual(response.status_code, 200)

    def test_physio_dashboard_protection(self):
        """
        Security test: Ensure that a user with a Client role 
        is blocked from accessing the Physiotherapist's private schedule.
        """
        self.client.login(username='client_user', password='password123')
        response = self.client.get(reverse('physio_schedule'))
        # Should redirect (302) due to user_passes_test decorator
        self.assertEqual(response.status_code, 302)

    def test_booking_process_success(self):
        """
        Happy Path: Verify that a client can book an available slot,
        the status updates to 'booked', and the user is redirected to their dashboard.
        """
        self.client.login(username='client_user', password='password123')
        url = reverse('book_slot', args=[self.slot.id])
        response = self.client.post(url, {'client_note': 'Test note'})

        # Refresh slot data from database
        self.slot.refresh_from_db()
        self.assertEqual(self.slot.status, 'booked')
        self.assertEqual(self.slot.client, self.client_user)
        self.assertRedirects(response, reverse('client_dashboard'))

    def test_prevent_booking_past_date(self):
        """
        Defensive Design: Ensure that the system prevents booking slots 
        that occur in the past, even if a POST request is sent directly.
        """
        # Create a slot in the past (yesterday)
        past_slot = BookingSlot.objects.create(
            physiotherapist=self.physio_profile,
            date=timezone.now().date() - datetime.timedelta(days=1),
            start_time=datetime.time(10, 0),
            end_time=datetime.time(11, 0),
            status='available'
        )
        self.client.login(username='client_user', password='password123')
        url = reverse('book_slot', args=[past_slot.id])
        response = self.client.post(url)

        # Verify status remains 'available' and was not changed
        past_slot.refresh_from_db()
        self.assertEqual(past_slot.status, 'available')
