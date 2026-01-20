from django.urls import path
from .views import booking_page, book_slot

urlpatterns = [
    path(
        "physio/<int:physio_id>/",
        booking_page,
        name="booking_page"
    ),
    path(
        "slot/<int:slot_id>/book/",
        book_slot,
        name="book_slot"
    ),
]
