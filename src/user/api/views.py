from rest_framework import generics
from .serializers import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


def get_user_token(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':  str(refresh),
        'access':   str(refresh.access_token),
    }


# user login view that also return token
class UserLoginView(generics.GenericAPIView):
    serializer_class=UserLoginSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data
        token=get_user_token(user)
        return Response({
            'user':serializer.data,
            'token':token,
        })
