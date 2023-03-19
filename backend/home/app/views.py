from rest_framework import generics, viewsets, status
from django.contrib.auth.models import User
from .models import Profile, Lightning
from .serializers import UserSerializer, LightningSerializer, ProfileSerializer, RegisterSerializer
from rest_framework.response import Response
from django.db.models import Q
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import filters
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView

class CreateProfile(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, *args, **kwargs):
        lightning = Profile.objects.get(user=self.request.user)
        lightning_data = ProfileSerializer(lightning).data
        return Response(data=lightning_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.save()
            Profile.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


my_profile = CreateProfile.as_view()

class LightningView(APIView):
    def get(self, *args, **kwargs):
            my_profile = Profile.objects.get(user=self.request.user)
            lightning_data = LightningSerializer().data
            return Response(data=lightning_data, status=status.HTTP_200_OK)

    def perform_update(self, serializer, *args, **kwargs):
        instance = serializer.save()
        instance.switch = True

lightning_view = LightningView.as_view()

class UserListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']

search = UserListView.as_view()

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def lightning(self, *args, **kwargs):
        serializer = RegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            user = serializer.save()
            Profile.objects.create(user=user)
            return Response({'success':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

register = RegisterAPI.as_view()

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

