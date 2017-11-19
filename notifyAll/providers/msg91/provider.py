#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.msg91.provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains the functionality of Msg91 Provider
"""

# future
from __future__ import unicode_literals

# 3rd party
import requests

# own app
from notifyAll import settings
from notifyAll.providers import base


class Msg91Provider(base.SMSProvider):
    """Mag91 Provider Class

    """
    id = 'msg91'
    name = 'msg91'

    def __init__(self, auth_key=None, *args, **kwargs):
        """

        :param auth_key: Msg91 auth key
        """

        super(Msg91Provider, self).__init__(*args, **kwargs)

        self.auth_key = auth_key

        # validate necessary settings and configure Msg91
        self._validate_configure_msg91()

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)

    def _validate_configure_msg91(self):
        """configure Msg91 client

        we will provide to ways to configure clients :
         - One, you can configure msg91 keys from environment variables if not,
         - Then Second, you can send keys as function arguments too,
         - Priority wil be given to function arguments

        :return: msg91 client instance
        """
        if self.auth_key is None:
            self.auth_id = getattr(settings, 'MSG91_AUTHKEY', None)

        if self.auth_key is None:
            raise RuntimeWarning(
                'to send sms via {0} you need to configure MSG91_AUTHKEY in \n'
                'environment variables or send auth_key as function arguments.'.format(self.name)
            )

    def _prepare_sms_message(self, from_, to, context):
        """Prepare msg91 message with necessary information.
        """
        sms_send_api = getattr(settings, 'MSG91_SMS_SEND_API')

        if type(to) is not list:
            to = [to, ]

        route = getattr(settings, 'MSG91_TRANSACTIONAL_ROUTE', 4)
        if context.get('transaction_message') is False or context.get('transaction_message') is None:
            route = getattr(settings, 'MSG91_PROMOTIONAL_ROUTE', 1)

        if context.get('country') is None:
            raise ValueError('country not found in context.')

        return sms_send_api.format(
            authkey=self.auth_key,
            mobiles=','.join(str(mobile) for mobile in to),
            message=context.get('body', ''),
            sender=from_,
            route=route,
            country=context.get('country', '')
        )

    def notify(self):
        """notify respective recipient using plivo client

        """
        sms_send_api = self._prepare_sms_message(self.source, self.destination, self.context)
        return requests.get(sms_send_api)

RegisterProvider = Msg91Provider
