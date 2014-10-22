from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import mixins, generics, status, permissions

from models import *
from serializers import *


def get_user(viewobj):
    user = viewobj.request.user
    if user.is_anonymous():
        raise Http404
    return user


class Account(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):  # /account
    """
    Retrieves the account information
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return get_user(self)


class Tasks(generics.ListAPIView):  # /tasks
    """
    Lists the tasks available
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = get_user(self)

        if user.Profile.is_app:
            return self.queryset.filter(user=user.id)
        else:
            raise Http404


class TaskSelect(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):  # /tasks/<tid>
    """
    Accesses a specific task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self, tid=None):
        user = get_user(self)

        if user.Profile.is_app:
            return self.queryset.filter(user=user.id, id=tid)
        else:
            raise Http404


class Results(generics.ListAPIView):  # /results
    """
    Lists all results
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        user = get_user(self)
        return self.queryset.filter(user=user.id)


class ResultSelect(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):  # /results/<rid>
    """
    Accesses a specific result
    """
    queryset = Result.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self, rid=None):
        user = get_user(self)
        return self.queryset.filter(id=rid, user=user.id)


class ResultsTaskSelect(generics.ListAPIView):  # /results/task/<tid>
    """
    Lists all results for a specific task
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self, tid=None):
        user = get_user(self)
        return self.queryset.filter(task=tid, user=user.id)