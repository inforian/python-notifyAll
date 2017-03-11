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
from django.core.exceptions import ImproperlyConfigured

# local

# own app
from notifyAll.providers import base, provider_config


class PlivoProvider(base.SMSProvider):
    """Plivo Provider Class

    """
    id = 'plivo'
    name = 'Plivo'

    def __init__(self, source, destination, notification_type, context):
        """

        :data: a dict contains all necessary data needed by Provider to send notification.
        """
        super(PlivoProvider, self).__init__()

        # validate necessary settings and configure Twilio
        self._validate_configure_plivo()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(notification_type)

        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.context = context

    def _validate_configure_plivo(self):
        """configure plivo client

        :return: plivo clinet instance
        """

        auth_id = getattr(provider_config, 'PLIVO_AUTH_ID', None)
        auth_token = getattr(provider_config, 'PLIVO_AUTH_TOKEN', None)

        if auth_id is None or auth_token is None:
            raise ImproperlyConfigured(
                'to send sms via {0} you need to configure PLIVO_AUTH_ID & PLIVO_AUTH_TOKEN in settings.'.format(self.name)
            )

        self.plivo_clinet = plivo.RestAPI(auth_id, auth_token)

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
