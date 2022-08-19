from django.urls import path

from user.api.views import (
    UserLoginView,
)

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
]
