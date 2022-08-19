from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from utils.base_errors import BaseErrors


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        fields = ['email', 'password']

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        raise serializers.ValidationError({'error': BaseErrors.invalid_email_or_password})

    def save(self, validated_data):
        refresh = RefreshToken.for_user(validated_data)
        return ({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
