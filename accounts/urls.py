from django.urls import path
from . import views

urlpatterns = [
    path(
        "profile/<int:pk>/",
        views.profile,
        name="profile",
    ),
    path(
        "update_profile/<int:pk>/",
        views.ProfileUpdate.as_view(),
        name="profile_update",
    ),
    path(
        "change_password/",
        views.ChangePassword.as_view(),
        name="password_change",
    ),
]
