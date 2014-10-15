from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import generics
from rest_framework import status

from models import *
from serializers import *


class AuthFilterMixin(generics.GenericAPIView):
    objectset = None
    auth_type = None # 'User', 'App', or 'All'

    def get_queryset(self):
        result = self.objectset
        if self.auth_type == "User":
            result = self.objectset.filter(user=self.request.user)
        elif self.auth_type == "App":
            result = self.objectset.filter(user=self.request.user, )


class AccountInfo(AuthFilterMixin, generics.RetrieveUpdateDestroyAPIView): # /account/info
    objectset = User.objects.all()
    auth_type = 'User'
    serializer_class = UserSerializer
