from rest_framework import generics
from post.models import Post as PostModel
from post.api.serializers import PostListSerializer


class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer

