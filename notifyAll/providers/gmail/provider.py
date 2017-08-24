#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.gmail.provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains the functionality of Gmail Provider
"""

# future
from __future__ import unicode_literals

# 3rd party
from gmail import GMail, Message

# own app
from notifyAll import settings
from notifyAll.providers import base


class GmailProvider(base.EmailProvider):
    """Gmail Provider Class

    :param username: Email client username
    :param password: Email client password
    """
    id = 'gmail'
    name = 'Gmail'

    def __init__(self, username=None, password=None, *args, **kwargs):
        """

        """
        super(GmailProvider, self).__init__(*args, **kwargs)

        # connection related settings
        self.username = username
        self.password = password

        # validate necessary settings are configured by user for Gmail
        # first we will check have user sent Gmail username / password via function
        # argument if not then we will check
        # env variable if both of them are not present then raise error.
        if self.username is None :
            self.username = getattr(settings, 'GMAIL_USERNAME', None)

        if self.password is None :
            self.password = getattr(settings, 'GMAIL_PASSWORD', None)

        if self.username is None or self.password is None:
            raise RuntimeWarning(
                'to send emails via {0} you need to configure username & password. \n'
                'Either send them as function argument via key \n'
                '`username` & `password` or set up env variable \n'
                'as `GMAIL_USERNAME` & `GMAIL_PASSWORD`.'.format(self.name)
            )

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)
        self.notify()

    def _make_connection(self):
        """make connection with backend

        :return: connection with gmail provider
        """
        return GMail(self.username, self.password)

    def _prepare_email_message(self):
        """Prepare email message for Gmail

        :return: Gmail Email message
        """
        message = {
            'subject': self.subject,
            'text': self.body,
            'sender': self.source,
            'to': self.destination,
            'cc': self.cc,
            'bcc': self.bcc,
        }

        if self.attachment:
            message.update({'attachments': list(self.attachment)})

        if self.html_message:
            message.update({'html': self.html_message})

        return Message(**message)

    def notify(self):
        """
        """
        gmail = self._make_connection()
        data = self._prepare_email_message()

        try:
            return gmail.send(data)
        except Exception as e:
            return e

RegisterProvider = GmailProvider
