from django.forms import widgets
from rest_framework import serializers

from api_v1.models import *


class UserSerializer(serializers.Serializer):
    pk = serializers.Field()

    username = serializers.CharField(max_length=32, unique=True, required=True)
    email = serializers.CharField(max_length=254, required=True)
    password = serializers.CharField(max_length=60, required=True)
    points = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update object instance
            instance.username = attrs.get('username', instance.username)
            instance.email = attrs.get('email', instance.email)
            instance.password = User.password_crypt(attrs.get('password', instance.password))
            return instance

        # Create new instance
        return User(**attrs)
