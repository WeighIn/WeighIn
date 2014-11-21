from django.conf.urls import patterns, include, url
from WeighIn import settings_prod_web

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/', 'django.views.static.serve', {'document_root': settings_prod_web.STATIC_ROOT}),
    url(r'^/?', include('frontsite.urls')),
)


