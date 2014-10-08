from django.conf.urls import patterns, include, url
from WeighIn import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeighIn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    (r'^static/', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
