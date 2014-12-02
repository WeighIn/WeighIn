from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url('^main/?$', TemplateView.as_view(template_name='main.html'), name='main'),
    url('^about/?$', TemplateView.as_view(template_name='aboutus.html'), name='about'),
    url('^login/?$', TemplateView.as_view(template_name='login.html'), name='login'),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^games/?$', TemplateView.as_view(template_name='games.html'), name='games'),
)
