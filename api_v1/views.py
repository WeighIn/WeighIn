from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import mixins, generics, status, permissions

from models import *
from serializers import *


class AccountInfo(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin): # /account/info
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return self.request.user

class AppTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(app=self.request.user)

class AppTask(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id'
