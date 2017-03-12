#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from example.demo import views

urlpatterns = [

    url(r'^$',
        views.home,
        name='home'),

    url(r'^notification/(?P<action>[a-z]+)/$',
        views.notification_handler,
        name='notification'),

]
