from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("physio/<int:physio_id>/", views.booking_page, name="booking_page"),
    path("slot/<int:slot_id>/book/", views.book_slot, name="book_slot"),
]
