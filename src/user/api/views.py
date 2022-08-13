from multiprocessing import get_context
from rest_framework import generics
from .serializers import UserLoginSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


# user login view that also return token
class UserLoginView(generics.GenericAPIView):
    serializer_class=UserLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data
        token=RefreshToken.for_user(user)
        return Response({
            'user':UserSerializer(user,context=self.get_serializer_context()).data,
            'token':str(token),
        })

class UserRegisterView(generics.GenericAPIView):
    serializer_class=UserSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        user=serializer.save()
        token=RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'token':str(token)
        })        
   