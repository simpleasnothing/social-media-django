from django.urls import path

from post.api.views import (
    PostListView
)

app_name = 'post'
urlpatterns = [
    path('', PostListView.as_view(), name='list_post'),
]
