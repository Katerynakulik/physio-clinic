from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Public pages
    path("", include("clinic.urls")),

    # Accounts (custom login/logout/redirects)
    path("accounts/", include("accounts.urls")),

    # Booking
    path("booking/", include("bookings.urls")),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )