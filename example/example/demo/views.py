#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render


def home(request):
    """
    """
    template_name = 'notification.html'

    return render(request, template_name)


def notification_handler(request, action):
    """
    """
    template_name = 'notification.html'
    if action == 'email':
        pass
    elif action == 'sms':
        pass
    elif action == 'push':
        pass

    return render(request, template_name)
