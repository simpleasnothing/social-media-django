from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate
from utils.base_errors import BaseErrors


class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True)
    
    def validate(self, attrs):
        user =authenticate(**attrs)
        if user:
            return user
        raise serializers.ValidationError(BaseErrors.user_login_invalid)
    
 


        
