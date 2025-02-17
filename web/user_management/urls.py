from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserProfileView,
    ChangePasswordView,
    UserListAdminView,
    UserDetailAdminView,
    UserRegistrationAdminView,
)

urlpatterns = [
    # JWT endpoints.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User endpoints.
    path('api/user/profile/', UserProfileView.as_view(), name='user_profile'),
    path('api/user/change-password/', ChangePasswordView.as_view(), name='change_password'),

    # Admin endpoints.
    path('api/admin/users/', UserListAdminView.as_view(), name='admin_user_list'),
    path('api/admin/users/<int:id>/', UserDetailAdminView.as_view(), name='admin_user_detail'),
    path('api/admin/users/register/', UserRegistrationAdminView.as_view(), name='admin_user_register'),
]
