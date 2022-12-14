from django.contrib.admin import AdminSite
from django.urls import path

from aimtravel_app.user_auth.views import SignUpView, SignInView, SignOutView, auth_option

urlpatterns = (
    path('', auth_option, name='auth option'),
    path('register/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    )
