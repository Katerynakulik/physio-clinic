from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import RoleBasedLoginView

urlpatterns = [
    path("register/", views.register_client, name="register"),

    path(
        "login/",
        RoleBasedLoginView.as_view(),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path(
        "client/dashboard/",
        views.client_dashboard,
        name="client_dashboard",
    ),

    path(
        "physio/dashboard/",
        views.physio_dashboard,
        name="physio_dashboard",
    ),
]