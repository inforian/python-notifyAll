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
from django.core.mail import EmailMultiAlternatives

# local
from notifyAll.services import service_config

# own app
from notifyAll.providers.gmail import gmail_provider_config
from notifyAll.providers import base


class GmailProvider(base.Provider):
    """Gmail Provider Class

    """
    id = 'gmail'
    name = 'Gmail'
    notify_type = service_config.EMAIL

    def __init__(self, source, destination, notification_type, context):
        """

        :data: a dict contains all necessary data needed by Provider to send notification.
        """

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(notification_type)

        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.context = context

    def _validate_notification_type_with_provider(self, notification_type):
        """validate notification_type w.r.t, means for which you have called this provider wether this provider
            allows that functionality ?

        :param notification_type: notification type (email, sms, push).
        """
        if not notification_type == self.notify_type:
            raise ValueError('Invalid notification type for Gmail Provider.')

    def _convert_var_type_to_list(self, value):
        """if value is not a list then convert that to list

        """
        return value if type(value) is list else [value]

    def _prepare_email_message(self):
        """Prepare email message with necessary information.
        """
        message = {
            'subject': self.context.get('subject', ''),
            'body': self.context.get('body', ''),
            'from_email': self.source if self.source else gmail_provider_config.EMAIL_HOST_USER,
            'to': self._convert_var_type_to_list(self.destination),
            'cc': self._convert_var_type_to_list(self.context.get('cc')),
            'bcc': self._convert_var_type_to_list(self.context.get('bcc')),
        }

        self.email_message = EmailMultiAlternatives(**message)

        if self.context.get('attachment'):
            self.email_message.attach_file(self.context.get('attachment'))

        if self.context.get('html_message'):
            self.email_message.attach_alternative(
                self.context.get('html_message'), 'text/html')

    def notify(self):
        """notify respective recipient using gmail smtp server

        """
        self._prepare_email_message()
        return self.email_message.send()

RegisterProvider = GmailProvider
