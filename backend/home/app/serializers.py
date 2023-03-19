from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Lightning, Profile
from rest_framework.fields import CurrentUserDefault
from .models import Profile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'password',
        ]

class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = Profile
        fields = [
            'pk',
            'user',
        ]

class LightningSerializer(serializers.ModelSerializer):
    user = serializers.CharField(default=CurrentUserDefault())
    class Meta:
        model = Lightning
        fields = [
            'pk',
            'user',
            'switch',
        ]

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

