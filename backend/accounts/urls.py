from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)


urlpatterns = [
    #path('signup',SignupView.as_view(), name='signup'),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', getUserProfile, name='user_profile'),
    path('users/',getUsers, name='users'),
    path('users/register/', registerUser, name='register'),

]