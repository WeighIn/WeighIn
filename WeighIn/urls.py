from django.conf.urls import patterns, include, url
from WeighIn import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1/', include('api.urls')),
    (r'^static/', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
