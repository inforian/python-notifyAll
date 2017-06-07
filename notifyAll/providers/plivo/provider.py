#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.plivo.provider
~~~~~~~~~~~~~~

- This file contains the functionality of Plivo Provider
"""

# future
from __future__ import unicode_literals

# 3rd party
import plivo

# Django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# local

# own app
from notifyAll.providers import base


class PlivoProvider(base.SMSProvider):
    """Plivo Provider Class

    """
    id = 'plivo'
    name = 'Plivo'

    def __init__(self, auth_id=None, auth_token=None, *args, **kwargs):
        """
       we will provide to ways to configure clients :
         - One, you can configure email settings from Django-settings file if not,
         - Then Second, you can send settings as function arguments too,
         - Priority wil be given to function arguments

        :param auth_id: plivo auth id
        :param auth_token: plivo auth token
        """

        super(PlivoProvider, self).__init__(*args, **kwargs)

        self.auth_id = auth_id
        self.auth_token = auth_token

        # validate necessary settings and configure Twilio
        self._validate_configure_plivo()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)


    def _validate_configure_plivo(self):
        """configure plivo client

        we will provide to ways to configure clients :
         - One, you can configure plivo keys from settings if not,
         - Then Second, you ca send keys as function arguments too,
         - Priority wil be given to function arguments

        :return: plivo client instance
        """
        if self.auth_id is None:
            self.auth_id = getattr(settings, 'PLIVO_AUTH_ID', None)
        if self.auth_token is None:
            self.auth_token = getattr(settings, 'PLIVO_AUTH_TOKEN', None)

        if self.auth_id is None or self.auth_token is None:
            raise ImproperlyConfigured(
                'to send sms via {0} you need to configure PLIVO_AUTH_ID & PLIVO_AUTH_TOKEN in settings.'.format(self.name)
            )

        self.plivo_clinet = plivo.RestAPI(self.auth_id, self.auth_token)

    def _prepare_sms_message(self, from_, to, context):
        """Prepare plivo message with necessary information.
        """
        return {
            'src': from_,
            'dst': to,
            'text': context.get('body', ''),
            'method': context.get('method', 'GET')
        }

    def notify(self):
        """notify respective recipient using plivo client

        """
        message = self._prepare_sms_message(self.source, self.destination, self.context)

        return self.plivo_clinet.send_message(message)

RegisterProvider = PlivoProvider
