from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from rest_framework.permissions import DjangoModelPermissions

from models import *
from serializers import *


def get_user(view):
    user = view.request.user
    if user.is_anonymous():
        raise PermissionDenied
    return user


class UserAccount(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return get_user(self)


class ApplicationTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'app'


class ApplicationTaskSelect(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
