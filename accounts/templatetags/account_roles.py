"""
Custom template tags for the accounts app.
This module provides filters to check user roles within Django templates,
enabling conditional rendering of UI elements based on profile types.
"""
from django import template

register = template.Library()


@register.filter
def has_client_profile(user):
    """
    Check if a user is associated with a ClientProfile.

    Args:
        user (User): The user object to check, typically from request.user.

    Returns:
        bool: True if user is authenticated and has a clientprofile attribute,
              False otherwise.
    """
    if not user or not getattr(user, "is_authenticated", False):
        return False
    return hasattr(user, "clientprofile")


@register.filter
def has_physio_profile(user):
    """
    Check if a user is associated with a Physiotherapist profile.

    Args:
        user (User): The user object to check, typically from request.user.

    Returns:
        bool: True if user is authenticated and has a physiotherapist attribute
              False otherwise.
    """
    if not user or not getattr(user, "is_authenticated", False):
        return False
    return hasattr(user, "physiotherapist")
