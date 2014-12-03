from django.conf.urls import patterns, include, url

from api_v1 import views

urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^test/', views.test),
    url(r'^login/', views.login_user),
    url(r'^hard_begin/', views.hard_begin),
    url(r'^hard_submit/', views.hard_submit),
    url(r'^user/?$', views.UserAccount.as_view()),

    url(r'^app/(?P<app_id>[0-9]+)', include([
        url(r'^/?$', views.ApplicationAccount.as_view()),

        url(r'^/tasks', include([
            url(r'^/?$', views.ApplicationTasks.as_view()),

            url(r'^/(?P<task_id>[0-9]+)', include([
                url(r'^/?$',  views.ApplicationTaskSelect.as_view()),

                url(r'^/results/?$', views.ApplicationResultsTaskSelect.as_view()),
            ])),
        ])),

        url(r'^/results', include([
            url(r'^/?$', views.ApplicationResults.as_view()),

            url(r'^/(?P<result_id>[0-9]+)/?$', views.ApplicationResultSelect.as_view()),

            url(r'^/task/(?P<task_id>[0-9]+)/?$', views.ApplicationResultsTaskSelect.as_view()),
        ])),
    ])),
)
