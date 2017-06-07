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
from django.conf import settings
from django.core.mail import get_connection

# local

# own app
from notifyAll.providers import base


class GmailProvider(base.EmailProvider):
    """Gmail Provider Class

    :param username: Email client username
    :param password: Email client password
    """
    id = 'gmail'
    name = 'Gmail'

    def __init__(self, username=None, password=None, *args, **kwargs):
        """

        """
        super(GmailProvider, self).__init__(*args, **kwargs)

        # connection related settings
        self.username = username
        self.password = password

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)
        self.notify()

    def _make_connection(self):
        """make connection with backend

        :return: connection with email provider
        """
        configuration = {
            'username': self.username,
            'password': self.password,
        }

        return get_connection(backend=settings.EMAIL_BACKEND,
                              fail_silently=self.fail_silently,
                              **configuration)

RegisterProvider = GmailProvider
