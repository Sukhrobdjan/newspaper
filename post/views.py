from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView


class UsersListView(ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

        

class UserDetailView(RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

        