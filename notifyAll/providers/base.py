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
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

# local
from notifyAll.services import service_config


class EmailProvider(object):
    """Base class for All email providers

    """
    id = None
    name = None
    notify_type = service_config.EMAIL

    def __init__(self, source, destination, notification_type, context,
                fail_silently=False):
        """
       we will provide to ways to configure clients :
         - One, you can configure email settings from Django-settings file if not,
         - Then Second, you can send settings as function arguments too,
         - Priority wil be given to function arguments

        :param source: who wants to send SMS
        :param destination: to whom SMS will be sent.
        :param notification_type: notification type
        :param context: data you want to send in SMS
        :param fail_silently: catch exception
        """

        # email related stuff
        self.source = settings.DEFAULT_FROM_EMAIL if source is None else source
        self.destination = destination
        self.notification_type = notification_type
        self.subject = context.get('subject', '')
        self.body = context.get('body', '')
        self.cc = context.get('cc')
        self.bcc = context.get('bcc')
        self.attachment = context.get('attachment')
        self.html_message = context.get('html_message')

        self.fail_silently = fail_silently

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

    def _make_connection(self):
        """make connection with backend

        :return: connection with email provider
        """
        return None

    def _prepare_email_message(self):
        """Prepare email message with necessary information.
        """

        message = {
            'subject': self.subject,
            'body': self.body,
            'from_email': self.source,
            'to': self._convert_var_type_to_list(self.destination),
            'cc': self._convert_var_type_to_list(self.cc),
            'bcc': self._convert_var_type_to_list(self.bcc),
            'connection': self._make_connection()
        }

        self.email_message = EmailMultiAlternatives(**message)

        if self.attachment:
            self.email_message.attach_file(self.attachment)

        if self.html_message:
            self.email_message.attach_alternative(
                self.html_message, 'text/html')

    def notify(self):
        """
        """
        self._prepare_email_message()
        return self.email_message.send()


class SMSProvider(object):
    """Base class for All SMS providers

    """
    id = None
    name = None
    notify_type = service_config.SMS

    def __init__(self, source, destination, notification_type, context):
        """

        :param source: who wants to send SMS
        :param destination: to whom SMS will be sent.
        :param notification_type: notification type
        :param context: data you want to send in SMS
        """
        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(notification_type)

        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.context = context

    def _validate_notification_type_with_provider(self, notification_type):
        """validate notification_type w.r.t notify_type of Provider, means for which you have called this provider
        wether this provider allows that functionality ?
        """
        if not notification_type == self.notify_type:
            raise ValueError('Invalid notification type for {0} Provider.'.format(self.name))

    def _prepare_sms_message(self, from_, to, context):
        """Prepare sms message with necessary information.
        """
        pass

    def notify(self):
        """
        """
        pass
