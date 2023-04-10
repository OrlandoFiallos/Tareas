from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Tasks
from .serializers import UserSerializer, TasksSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
