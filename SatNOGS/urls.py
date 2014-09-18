# -*- coding: utf-8 -*-
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
    url(r'^stations/json/$', 'base.views.stations_json', name='stations_json'),
    url(r'^observations/$', 'base.views.observations_list', name='observations'),

    url(r'^about/$',
        TemplateView.as_view(template_name='base/about.html'),
        name='about'),
    url(r'^stations/$',
        TemplateView.as_view(template_name='base/stations.html'),
        name='stations'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^avatar/', include('avatar.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
