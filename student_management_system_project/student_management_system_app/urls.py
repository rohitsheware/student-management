from django.urls import path
from student_management_system_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration/", views.registration, name="registration"),
    path("data/", views.data, name="data"),
    path("login/", views.logged, name="login"),
    path("signup/", views.signup, name="signup"),
    path("remove/<int:id>/", views.remove, name="remove"),
    path("logout/", views.Log_Out, name="logout"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="register/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="register/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="register/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="register/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
