from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import PermissionDenied

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import mixins, generics, status
from rest_framework.permissions import DjangoModelPermissions
import json
from django.http import HttpResponse

from models import *
from serializers import *


def test(request):
    response_data = {}
    response_data['game_num'] = '0'
    response_data['game_data'] = ['blah', 'blah1', 'blah3']
    response_data['username'] = request.GET.get('q', '')
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def login(request):
    response_data = {}
    username = request.GET.get('username', 'null')
    password = request.GET.get('password', 'null')

    if username == 'Andrew' and password == '1234':
        response_data['points'] = 400
        response_data['success'] = 'True'
        response_data['username'] = 'Andrew'
    else:
        response_data['success'] = 'False'
    return HttpResponse(json.dumps(response_data), content_type="application/json")



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
            app_id=self.kwargs['app_id']
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
            task_id=self.kwargs['task_id']
        )


class ApplicationResults(generics.ListAPIView):
    permission_classes = (DjangoModelPermissions,)
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Result.objects.filter(
            task_id__app_id=self.kwargs['app_id']
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
            task_id=self.kwargs['task_id']
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
            result_id=self.kwargs['result_id']
        )
