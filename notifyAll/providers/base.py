#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.base
~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains the base class for all providers

General Instructions for creating providers :

- `id` and provider `app_name` must be same.
    e.g., for `gmail` provider , id is 'gmail' and app_name is also 'gmail'.

"""

# future
from __future__ import unicode_literals

# local
from notifyAll import settings


class EmailProvider(object):
    """Base class for All email providers

    """
    id = None
    name = None
    notify_type = settings.EMAIL

    def __init__(self, source, destination, notification_type, context):
        """
       we will provide to ways to configure clients :
         - One, you can configure email settings from Django-settings file if not,
         - Then Second, you can send settings as function arguments too,
         - Priority wil be given to function arguments

        :param source: who wants to send SMS
        :param destination: to whom SMS will be sent.
        :param notification_type: notification type
        :param context: data you want to send in SMS
        """

        # email related stuff
        self.source = source
        self.destination = destination
        self.notification_type = notification_type
        self.subject = context.get('subject', '')
        self.body = context.get('body', '')
        self.cc = context.get('cc')
        self.bcc = context.get('bcc')
        self.attachment = context.get('attachment')
        self.html_message = context.get('html_message')

    def _validate_notification_type_with_provider(self, notification_type):
        """validate notification_type w.r.t notify_type of Provider, means for which you have called this provider
        whether this provider allows that functionality ?
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
        pass

    def notify(self):
        """
        """
        pass


class SMSProvider(object):
    """Base class for All SMS providers

    """
    id = None
    name = None
    notify_type = settings.SMS

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
