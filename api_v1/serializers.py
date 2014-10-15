from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User

from api_v1.models import *


class UserSerializer(serializers.ModelSerializer):
    Profile = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        read_only_fields = ('id', 'username')
        write_only_fields = ('password',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'app', 'worth', 'accuracy', 'data')
        read_only_fields = ('id', 'app')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'task', 'user', 'submit_date', 'data')
        read_only_fields = ('id', 'task', 'user', 'submit_date', 'data')
