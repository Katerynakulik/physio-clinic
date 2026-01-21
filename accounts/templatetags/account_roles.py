from django import template

register = template.Library()


@register.filter
def has_client_profile(user):
    """Return True if the user has a related ClientProfile."""
    if not user or not getattr(user, "is_authenticated", False):
        return False
    return hasattr(user, "clientprofile")


@register.filter
def has_physio_profile(user):
    """Return True if the user has a related Physiotherapist."""
    if not user or not getattr(user, "is_authenticated", False):
        return False
    return hasattr(user, "physiotherapist")
