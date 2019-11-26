from django.contrib.auth.models import User, Group
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from quickstart.serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
