from django.conf.urls import patterns, include, url

from api_v1 import views

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),

    url(r'^account/?$', views.UserAccount.as_view()),

    url(r'^tasks', include([
#        url(r'^/?$', views.Tasks.as_view()),

#        url(r'^/(?P<tid>[0-9]+)/?$', views.TaskSelect.as_view()),
    ])),

    url(r'^results', include([
#        url(r'^/?$', views.Results.as_view()),

#        url(r'^/(?P<rid>[0-9]+)/?$', views.ResultSelect.as_view()),

#        url(r'^/task/(?P<tid>[0-9]+)/?$', views.ResultsTaskSelect.as_view()),
    ])),
)
