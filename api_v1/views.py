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
from django.contrib.auth import authenticate, login

from models import *
from serializers import *
from models import Profile


def test(request):
    response_data = {}
    response_data['game_num'] = '0'
    response_data['game_data'] = ['blah', 'blah1', 'blah3']
    response_data['username'] = request.GET.get('q', '')
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def fake_login(username,password):
    if username == 'Andrew' and password == '1234':
        return True
    else:
        return False

def hard_submit(request):
    response_data = {}
    response_data['response_type'] = 'submit'
    response_data['delta_points'] = 5
    response_data['points'] = 405
    response_data['game_num'] = 0
    response_data['items'] = 6
    response_data['item_0'] = {'score': 10}
    response_data['item_1'] = {'score': 2}
    response_data['item_2'] = {'score': 3}
    response_data['item_3'] = {'score': 4}
    response_data['item_4'] = {'score': 5}
    response_data['item_5'] = {'score': 8}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def login_user(request):
    response_data = {}
    username = request.GET.get('username', 'null')
    password = request.GET.get('password', 'null')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response_data['points'] = 400
            response_data['success'] = 'True'
            response_data['username'] = username
            # p = Profile(user_id =user, points = 0, name = 'Andrew')
            # p.save()
        else:
            response_data['success'] = 'False'
    else:
        response_data['success'] = 'False'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def hard_game_num_request(request):
    response_data = {}
    response_data['game_num'] = 0
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def hard_game_begin(request):
    response_data = {}
    if request.GET.get('game_num', 'null') == str(0):
        response_data['item_0'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task0.png'}
        response_data['item_1'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task1.png'}
        response_data['item_2'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task2.png'}
        response_data['item_3'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task3.png'}
        response_data['item_4'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task4.png'}
        response_data['item_5'] = {'source': 'https://s3.amazonaws.com/weighin/game0/task5.png'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def viewaccount(view):
    user = view.request.user
    return user

# def login(request):
#     response_data = {}
#     username = request.GET.get('username', 'null')
#     password = request.GET.get('password', 'null')
#
#     if fake_login(username, password):
#         response_data['points'] = 400
#         response_data['success'] = 'True'
#         response_data['username'] = 'Andrew'
#     else:
#         response_data['success'] = 'False'
#     return HttpResponse(json.dumps(response_data), content_type="application/json")



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
