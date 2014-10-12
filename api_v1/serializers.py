from django.forms import widgets
from rest_framework import serializers

from api_v1.models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.Field()
    username = serializers.CharField(max_length=32, unique=True, required=True)
    email = serializers.CharField(max_length=254, required=True)
    password = serializers.CharField(max_length=60, required=True)
    points = serializers.IntegerField(default=0)

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'points')
        read_only_fields = ('id', 'points', 'username')
        write_only_fields = ('password',)


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'owner', 'app_key')
        read_only_fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'application', 'worth', 'accuracy', 'data')
        read_only_fields = ('id', 'application')


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'task', 'user', 'submit_date', 'data')
        read_only_fields = ('id', 'task', 'user', 'submit_date', 'data')
