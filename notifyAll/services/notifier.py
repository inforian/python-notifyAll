#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.services.notifier
~~~~~~~~~~~~~~

-  This file contains the library common file, every request for sending notifications will come here,
   Here we will route notification to its respective Provider
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.utils.module_loading import import_string

# local

# own app
from notifyAll.services import service_config


class Notifier(object):
    """

    """
    def __init__(self, source, destination, notification_type, provider, context):
        """

        :param source: who wants to send the notification.
        :param destination: to whom you want to send notification.
        :param notification_type: notification type (email, sms, push).
        :param provider: notification Provider.
        :param context: Context/data you want send in notification.
        """

        # validate notification_type
        self._validate_notification_type(notification_type)

        # validate provider type
        self.provider = self._validate_provider(provider)

        # validate context , it must be a dict()
        if type(context) is not dict:
            raise ValueError('context must be of dict() type not {0}.'.format(type(context)))

        self.data = {
            'source': source,
            'destination': destination,
            'notification_type': notification_type,
            'context': context,
        }

    def _validate_notification_type(self, notification_type):
        """validate notification_type, wether we have service of requested notification_type or not.

        :param notification_type: notification type (email, sms, push).
        """
        if notification_type not in service_config.ALLOWED_SERVICES:
            raise ValueError('Invalid notification type. Valid values are {0}.'.format(service_config.ALLOWED_SERVICES))

    def _validate_provider(self, provider):
        """validate provider, wether we have integrated requested provider or not.

        :param provider: notification Provider.
        :return: provider class Instance (if provider is valid)
        """
        provider_app_path = service_config.PROVIDER_APP_CLASS_PATH.format(provider)

        try:
            return import_string(provider_app_path)  # import provider app dynamically
        except ImportError:
            raise ValueError('Invalid provider {0} selected'.format(provider))

    def notify(self):
        """route notification to its respective Provider

        """
        provider_instance = self.provider(**self.data)
        provider_instance.notify()
