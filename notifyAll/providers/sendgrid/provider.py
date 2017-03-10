#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.sendgrid.provider
~~~~~~~~~~~~~~

- This file contains the functionality of SendGrid Provider
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# local

# own app
from notifyAll.providers import base


class SendGridProvider(base.EmailProvider):
    """SendGrid Provider Class

    """
    id = 'sendgrid'
    name = 'SendGrid'

    def __init__(self, source, destination, notification_type, context):
        """

        :data: a dict contains all necessary data needed by Provider to send notification.
        """
        super(SendGridProvider, self).__init__()

        # validate necessary settings are configured by user for SendGrid
        sendgrid_api_key = getattr(settings, 'SENDGRID_API_KEY', None)

        if sendgrid_api_key is None:
            raise ImproperlyConfigured(
                'to send emails via {0} you need to configure SENDGRID_API_KEY in settings.'.format(self.name)
            )

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

RegisterProvider = SendGridProvider
