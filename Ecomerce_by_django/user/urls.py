from django.urls import path
from .views import UserRegisterView , UserOrderDetailView , UpdateProfileView , UpdateUserRoleView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)



urlpatterns = [
    path('register/' , UserRegisterView.as_view()),
    path('order/details' , UserOrderDetailView.as_view()),
    path('profile' , UpdateProfileView.as_view()),
    path('users/<int:pk>/role' , UpdateUserRoleView.as_view()),


    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]