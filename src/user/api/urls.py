from django.urls import path
from user.api.views import UserLoginView, UserRegisterView

app_name='user'
urlpatterns=[
   
    path('login/',UserLoginView.as_view(),name='user-login'),
    path('register/',UserRegisterView.as_view(),name='user-register'),
]
