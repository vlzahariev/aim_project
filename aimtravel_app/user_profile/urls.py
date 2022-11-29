from django.urls import path, include

from aimtravel_app.user_profile.views import EditUserProfileView, UserProfileView, EmployeeProfileView, AllEmployeeView

urlpatterns = (
    path('profile/', include([
        path('edit/<int:pk>/', EditUserProfileView.as_view(), name='edit profile'),
        path('details/<int:pk>/', UserProfileView.as_view(), name='details profile'),
    ])),
    path('employee/', include([
        # path('edit/<int:pk>/', EditUserProfileView.as_view(), name='edit profile'),
        path('details/<int:pk>/', EmployeeProfileView.as_view(), name='employee details profile'),
    ])),
    path('company/', include([
        path('team/', AllEmployeeView.as_view(), name='team'),
    ])),
)
