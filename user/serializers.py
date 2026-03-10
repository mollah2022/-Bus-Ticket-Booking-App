from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import SiteUser

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ('id','username','email','password','phone_number','special_user')
        extra_kwargs = {
            'password': {'write_only': True},
            'phone_number': {'required': False},
            'special_user': {'required': False},
        }

    def create(self, validated_data):
        user = SiteUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
