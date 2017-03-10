#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.base
~~~~~~~~~~~~~~

- This file contains the base class for all providers

General Instructions for creating providers :

- `id` and provider `app_name` must be same.
    e.g., for `gmail` provider , id is 'gmail' and app_name is also 'gmail'.

"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.core.mail import EmailMultiAlternatives

# local
from notifyAll.services import service_config

# own app
from notifyAll.providers import provider_config


class EmailProvider(object):
    """Base class for All email providers

    """
    id = None
    name = None
    notify_type = service_config.EMAIL

    def _validate_notification_type_with_provider(self, notification_type):
        """validate notification_type w.r.t notify_type of Provider, means for which you have called this provider
        wether this provider allows that functionality ?
        """
        if not notification_type == self.notify_type:
            raise ValueError('Invalid notification type for {0} Provider.'.format(self.name))

    def _convert_var_type_to_list(self, value):
        """if value is not a list then convert that to list

        """
        return value if type(value) is list else [value]

    def _prepare_email_message(self, to, from_, context):
        """Prepare email message with necessary information.
        """
        message = {
            'subject': context.get('subject', ''),
            'body': context.get('body', ''),
            'from_email': to if to else provider_config.DEFAULT_FROM_EMAIL,
            'to': self._convert_var_type_to_list(from_),
            'cc': self._convert_var_type_to_list(context.get('cc')),
            'bcc': self._convert_var_type_to_list(context.get('bcc')),
        }

        self.email_message = EmailMultiAlternatives(**message)

        if context.get('attachment'):
            self.email_message.attach_file(context.get('attachment'))

        if context.get('html_message'):
            self.email_message.attach_alternative(
                context.get('html_message'), 'text/html')

    def notify(self):
        """
        """
        pass
