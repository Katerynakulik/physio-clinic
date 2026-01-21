from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public pages
    path("", include("clinic.urls")),

    # Accounts (custom login/logout/redirects)
    path("accounts/", include("accounts.urls")),

    # Booking
    path("booking/", include("bookings.urls")),
]
