from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = patterns(
    '',

    # Base urls
    url(r'^', include('network.base.urls', namespace='base')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('network.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^avatar/', include('avatar.urls')),

    url(r'^api/', include('network.api.urls'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
