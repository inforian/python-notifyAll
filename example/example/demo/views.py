#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from example.utils import notify


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
        html_message = None
        if request.POST.get('html_message') is True:
            html_message = request.POST.get('body')

        context = {
            'subject': request.POST.get('subject', ''),
            'body': request.POST.get('body', ''),
            'html_message': html_message
        }

        data = {
            'source': 'admin@example.com',
            'destination': request.POST.get('to'),
            'notification_type': 'email',
            'provider': request.POST.get('provider'),
            'context': context,
        }

        try:
            notify(**data)
            messages.add_message(request, messages.SUCCESS, 'Email successfully sent.')
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)

    elif action == 'sms':
        pass
    elif action == 'push':
        pass

    return redirect(reverse('home'))
