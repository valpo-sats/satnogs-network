from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', 'index', name='home'),
    url(r'^o/(?P<id>[0-9]+)/$',
        'view_observation', name='observations_view_observation'),
    url(r'^observations/$', 'observations_list',
        name='observations'),
    url(r'^observations/new/$', 'observation_new', name='observation_new'),
    url(r'^about/$',
        TemplateView.as_view(template_name='base/about.html'),
        name='about'),
    url(r'^stations/$', 'stations_list', name='stations'),
    url(r'^s/(?P<id>[0-9]+)/$',
        'base.views.view_station', name='stations_view_station'),
    url(r'^prediction_windows/(?P<sat_id>[\w.@+-]+)/(?P<start_date>.+)/(?P<end_date>.+)/$',
        'prediction_windows',
        name='prediction_windows'),
)
