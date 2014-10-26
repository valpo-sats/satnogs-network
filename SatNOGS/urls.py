from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'base.views.index', name='home'),

    # Observations
    url(r'^o/(?P<id>[0-9]+)/$',
        'base.views.view_observation', name='observations_view_observation'),
    url(r'^observations/$', 'base.views.observations_list',
        name='observations'),
    url(r'^observations/new/$', 'base.views.observation_new', name='observation_new'),
    url(r'^about/$',
        TemplateView.as_view(template_name='base/about.html'),
        name='about'),
    url(r'^stations/$',
        TemplateView.as_view(template_name='base/stations.html'),
        name='stations'),
    url(r'^prediction_windows/(?P<sat_id>[\w.@+-]+)/(?P<start_date>.+)/(?P<end_date>.+)/$',
        'base.views.prediction_windows',
        name='prediction_windows'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    url(r'^api/', include('base.api.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
