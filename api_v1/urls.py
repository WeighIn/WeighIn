from django.conf.urls import patterns, include, url

from api_v1 import views

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)
