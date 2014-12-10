from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User

from api_v1.models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('points',)
        read_only_fields = ('points',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        read_only_fields = ('username',)
        write_only_fields = ('password',)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('app_id', 'points')
        read_only_fields = ('app_id', 'points')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('task_id', 'app_id', 'worth', 'accuracy', 'data')
        read_only_fields = ('task_id', 'app_id', 'complete')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('result_id', 'task_id', 'user_id', 'submit_date', 'data')
        read_only_fields = ('result_id', 'task_id', 'user_id', 'submit_date', 'data')