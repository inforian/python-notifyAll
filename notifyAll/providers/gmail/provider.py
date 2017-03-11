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

# local

# own app
from notifyAll.providers import base


class GmailProvider(base.EmailProvider):
    """Gmail Provider Class

    """
    id = 'gmail'
    name = 'Gmail'

    def __init__(self, source, destination, notification_type, context):
        """

        :data: a dict contains all necessary data needed by Provider to send notification.
        """
        super(GmailProvider, self).__init__()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(notification_type)

        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.context = context

    def notify(self):
        """notify respective recipient using gmail smtp server

        """
        self._prepare_email_message(self.source, self.destination, self.context)
        return self.email_message.send()

RegisterProvider = GmailProvider
