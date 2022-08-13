from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate

User=get_user_model()

# serializer for register and get user details 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=('email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
 

# serializer for user login
class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()

    def validate(self, attrs):
        user =authenticate(**attrs)
        if user:
            return user
        return serializers.ValidationError("login error!")    
