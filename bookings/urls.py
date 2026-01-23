from django.urls import path
from . import views
from . import views_physio

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("physio/<int:physio_id>/", views.booking_page, name="booking_page"),
    path("slot/<int:slot_id>/book/", views.book_slot, name="book_slot"),
    path("slot/<int:slot_id>/cancel/", views.cancel_booking, name="cancel_booking"),


    # Physiotherapist schedule (role-protected)
    path("physio/schedule/", views_physio.physio_schedule, name="physio_schedule"),
    path("physio/slot/<int:slot_id>/block/", views_physio.block_slot, name="block_slot"),
    path("physio/slot/<int:slot_id>/cancel/", views_physio.cancel_booking_physio, name="cancel_booking_physio"),
    path("slot/<int:slot_id>/note/", views.update_physio_note, name="update_physio_note"),

]
