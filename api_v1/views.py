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


def get_user_id(view):
    return get_user(view).id


class UserAccount(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, queryset=None):
        return get_user(self)


class ApplicationAccount(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def post(self, request):
        serializer = ApplicationSerializer(user_id=get_user_id(self), data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Application.objects.filter(
            app_id=self.kwargs['app_id'],
            user_id=self.request.user.id
        )


class ApplicationTasks(generics.ListAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(
            app_id=self.kwargs['app_id'],
            user_id=get_user_id(self)
        )


class ApplicationTaskSelect(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request):
        serializer = TaskSerializer(app_id=self.kwargs['app_id'], data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Task.objects.filter(
            app_id=self.kwargs['app_id'],
            task_id=self.kwargs['task_id'],
            app_id__user_id=get_user_id(self)
        )


class ApplicationResults(generics.ListAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.filter(
            task_id__app_id=self.kwargs['app_id'],
            user_id=get_user_id(self)
        )


class ApplicationResultsTaskSelect(generics.ListAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def post(self, request):
        serializer = ResultSerializer(
            app_id=self.kwargs['app_id'],
            task_id=self.kwargs['task_id'],
            user_id=get_user_id(self),
            data=request.DATA
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Result.objects.filter(
            task_id__app_id=self.kwargs['app_id'],
            task_id=self.kwargs['task_id'],
            user_id=get_user_id(self)
        )


class ApplicationResultSelect(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def post(self, request):
        serializer = ResultSerializer(app_id=self.kwargs['app_id'], user_id=get_user_id(self), data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Result.objects.filter(
            task_id__app_id=self.kwargs['app_id'],
            result_id=self.kwargs['result_id'],
            user_id=get_user_id(self)
        )
