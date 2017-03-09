#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.gmail.provider
~~~~~~~~~~~~~~

- This file contains the functionality of Gmail Provider
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.core.mail import send_mail

# local

# own app
from notifyAll.providers.gmail import gmail_provider_config
from notifyAll.providers import base


class GmailProvider(base.Provider):
    """Gmail Provider Class

    """
    id = 'gmail'
    name = 'Gmail'
    notify_type = 'email'

    def __init__(self):
        """

        """

    def notify(self):
        """notify respective recipient using gmail smtp server
        """
        send_mail('Subject here', 'Here is the message.', gmail_provider_config.EMAIL_HOST_USER,
         ['neeraj.dhiman@veris.in'], fail_silently=False)


RegisterProvider = GmailProvider
