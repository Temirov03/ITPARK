from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import generics

from .models import NewUser


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class NewUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        fields = '__all__'

