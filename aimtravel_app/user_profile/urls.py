from django.urls import path, include

from aimtravel_app.user_profile.views import EditUserProfileView, UserProfileView

urlpatterns = (
    path('profile/', include([
        path('edit/<int:pk>/', EditUserProfileView.as_view(), name='edit profile'),
        path('details/<int:pk>/', UserProfileView.as_view(), name='details profile'),

    ])),
)
