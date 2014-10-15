from django.conf.urls import patterns, include, url

from api_v1 import views

urlpatterns = patterns('',
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/$', include('rest_framework_swagger.urls')),

    url(r'^account/info/?$', views.AccountInfo.as_view()),
    url(r'^app/tasks/?$', views.AppTasks.as_view()),
    url(r'^app/tasks/(?P<id>[0-9]+)/?$', views.AppTask.as_view()),
)
