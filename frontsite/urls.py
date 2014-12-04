from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^main/?$', TemplateView.as_view(template_name='main.html'), name='main'),
    url(r'^about/?$', TemplateView.as_view(template_name='aboutus.html'), name='about'),
    url(r'^login/?$', TemplateView.as_view(template_name='login.html'), name='login'),

	url(r'^games', include([
		url(r'^/?$', TemplateView.as_view(template_name='games.html'), name='games'),
		url(r'^/weighin/?$', TemplateView.as_view(template_name='games/weighin.html'), name='weighin_game'),
	]),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
)
