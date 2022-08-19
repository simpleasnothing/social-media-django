from rest_framework import generics
from rest_framework.response import Response

from user.api.serializers import LoginSerializer
from utils import BaseVersioning


class UserLoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    versioning_class = BaseVersioning

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = serializer.save(validated_data=serializer.validated_data)
        return Response(res)
