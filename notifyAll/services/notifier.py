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
        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.provider = provider
        self.context = context

        # validate notification_type
        self._validate_notification_type()

        # validate provider type
        self._validate_provider()

    def _validate_notification_type(self):
        """validate notification_type, wether we have service of requested notification_type or not.
        """
        if self.notification_type not in service_config.ALLOWED_SERVICES:
            raise ValueError('Invalid notification type. Valid values are {0}.'.format(service_config.ALLOWED_SERVICES))

    def _validate_provider(self):
        """validate provider, wether we have integrated requested provider or not.
        """
        provider_app_path = service_config.PROVIDER_APP_CLASS_PATH.format(self.provider)

        try:
            self.provider = import_string(provider_app_path)  # import provider app dynamically
        except ImportError:
            raise ValueError('Invalid provider {0} selected'.format(self.provider))

    def notify(self):
        """route notification to its respective Provider

        """
        provider_instance = self.provider()
        provider_instance.notify()
