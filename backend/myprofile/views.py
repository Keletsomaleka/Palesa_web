from django.shortcuts import render
from rest_framework import permissions
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ProfilesListView(ListAPIView):
    queryset = Profile.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = ProfileSerializer

class ProfileView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


