from django.urls import path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from .views import (
    ContactDetailView,
    ContactListView,
    MeView,
    SendEmailOTPView,
    SendOTPView,
    VerifyEmailOTPView,
    VerifyOTPView,
)

urlpatterns = [
    path("auth/email-otp/send", SendEmailOTPView.as_view(), name="email-otp-send"),
    path("auth/email-otp/verify", VerifyEmailOTPView.as_view(), name="email-otp-verify"),
    # Phone sign-in: kept only for accounts created before email sign-in (not used by the app).
    path("auth/otp/send", SendOTPView.as_view(), name="otp-send"),
    path("auth/otp/verify", VerifyOTPView.as_view(), name="otp-verify"),
    path("auth/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/logout", TokenBlacklistView.as_view(), name="logout"),
    path("me", MeView.as_view(), name="me"),
    path("me/contacts", ContactListView.as_view(), name="contact-list"),
    path("me/contacts/<uuid:pk>", ContactDetailView.as_view(), name="contact-detail"),
]
