from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Todo
        fields="__all__"

class SignUpSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)