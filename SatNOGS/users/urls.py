# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),

    # URL pattern for the UserDetailView
    url(r'^(?P<username>[\w.@+-]+)/$',
        'users.views.view_user', name='view_user'),
)
