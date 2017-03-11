#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.twilio.provider
~~~~~~~~~~~~~~

- This file contains the functionality of Twilio Provider
"""

# future
from __future__ import unicode_literals

# 3rd party
from twilio.rest import TwilioRestClient

# Django
from django.core.exceptions import ImproperlyConfigured

# local

# own app
from notifyAll.providers import base, provider_config


class TwilioProvider(base.SMSProvider):
    """Twilio Provider Class

    """
    id = 'twilio'
    name = 'Twilio'

    def __init__(self, source, destination, notification_type, context):
        """

        :data: a dict contains all necessary data needed by Provider to send notification.
        """
        super(TwilioProvider, self).__init__()

        # validate necessary settings and configure Twilio
        self._validate_configure_plivo()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(notification_type)

        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.context = context

    def _validate_configure_plivo(self):
        """configure twilio client

        :return: twilio client instance
        """

        account_sid = getattr(provider_config, 'TWILIO_ACCOUNT_SID', None)
        auth_token = getattr(provider_config, 'TWILIO_AUTH_TOKEN', None)

        if account_sid is None or auth_token is None:
            raise ImproperlyConfigured(
                'to send sms via {0} you need to configure TWILIO_ACCOUNT_SID & TWILIO_AUTH_TOKEN in settings.'.format(self.name)
            )

        self.twilio_clinet = TwilioRestClient(account_sid, auth_token)

    def notify(self):
        """notify respective recipient using twilio client

        """
        return self.twilio_clinet.messages.create(
            to=self.destination,
            from_=self.source,
            body=self.context.get('body', ''),
        )

RegisterProvider = TwilioProvider
