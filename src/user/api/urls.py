from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.api.views import UserLoginView, UserRegisterView

app_name='user'
urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/',UserLoginView.as_view(),name='user-login'),
    path('register/',UserRegisterView.as_view(),name='user-register'),
]