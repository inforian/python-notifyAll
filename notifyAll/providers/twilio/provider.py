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
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# local

# own app
from notifyAll.providers import base


class TwilioProvider(base.SMSProvider):
    """Twilio Provider Class

    """
    id = 'twilio'
    name = 'Twilio'

    def __init__(self, account_sid=None, auth_token=None, *args, **kwargs):
        """

        :param account_sid: twilio auth id
        :param auth_token: twilio auth token
        """
        super(TwilioProvider, self).__init__(*args, **kwargs)

        self.account_sid = account_sid
        self.auth_token = auth_token

        # validate necessary settings and configure Twilio
        self._validate_configure_twilio()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)

    def _validate_configure_twilio(self):
        """configure twilio client

        we will provide to ways to configure clients :
         - One, you can configure twilio keys from settings if not,
         - Then Second, you ca send keys as function arguments too,
         - Priority wil be given to function arguments

        :return: twilio client instance
        """

        if self.account_sid is None:
            self.account_sid = getattr(settings, 'TWILIO_ACCOUNT_SID', None)
        if self.auth_token is None:
            self.auth_token = getattr(settings, 'TWILIO_AUTH_TOKEN', None)

        if self.account_sid is None or self.auth_token is None:
            raise ImproperlyConfigured(
                'to send sms via {0} you need to configure TWILIO_ACCOUNT_SID & TWILIO_AUTH_TOKEN in settings.'.format(self.name)
            )

        self.twilio_clinet = TwilioRestClient(self.account_sid, self.auth_token)

    def notify(self):
        """notify respective recipient using twilio client

        """
        return self.twilio_clinet.messages.create(
            to=self.destination,
            from_=self.source,
            body=self.context.get('body', ''),
        )

RegisterProvider = TwilioProvider
