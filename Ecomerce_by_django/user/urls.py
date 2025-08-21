from django.urls import path
from .views import UserRegisterView , UserProfileView , UpdateProfileView , UpdateUserRoleView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('register/' , UserRegisterView.as_view()),
    path('profile' , UserProfileView.as_view()),
    path('update-profile' , UpdateProfileView.as_view()),
    path('update-user-role/<int:pk>' , UpdateUserRoleView.as_view()),


    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]