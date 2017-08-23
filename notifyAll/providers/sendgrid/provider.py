#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.sendgrid.provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file contains the functionality of SendGrid Provider
"""

# future
from __future__ import unicode_literals

# 3rd party
import sendgrid
from sendgrid.helpers.mail import Mail, Content, Personalization, Email

# local
from notifyAll import settings

# own app
from notifyAll.providers import base


class SendGridProvider(base.EmailProvider):
    """SendGrid Provider Class

    """
    id = 'sendgrid'
    name = 'SendGrid'

    def __init__(self, sendgrid_api_key=None, *args, **kwargs):
        """
        we will provide to ways to configure clients :
         - One, you can configure plivo keys from settings if not,
         - Then Second, you ca send keys as function arguments too,
         - Priority wil be given to function arguments

        :param sendgrid_api_key: SendGrid API key
        """
        super(SendGridProvider, self).__init__(*args, **kwargs)

        self.sendgrid_api_key = sendgrid_api_key

        # validate necessary settings are configured by user for SendGrid
        # first we will check have user sent sendgrid api key via function
        # argument if not then we will check
        # env variable if both of them are not present then raise error.
        if self.sendgrid_api_key is None:
            self.sendgrid_api_key = getattr(settings, 'SENDGRID_API_KEY', None)

        if self.sendgrid_api_key is None:
            raise RuntimeWarning(
                'to send emails via {0} you need to configure sendgrid api \n'
                'key.Either send them as function argument via key \n'
                '`sendgrid_api_key` or set up env variable \n'
                'as `SENDGRID_API_KEY`.'.format(self.name)
            )

        # validate notification_type w.r.t Provider notify_type
        self._validate_notification_type_with_provider(self.notification_type)
        self.notify()

    def _make_connection(self):
        """make connection with sendgrid

        :return: connection with email provider
        """

        return sendgrid.SendGridAPIClient(apikey=self.sendgrid_api_key)

    def _prepare_email_message(self):
        """Prepare email message for Sendgrid

        :return: Sendgrid Email message
        """
        mail = Mail()

        mail.from_email = Email(self.source)
        mail.subject = self.subject

        # personalization of email
        personalization = Personalization()

        # add multiple recipients
        for to_email in self._convert_var_type_to_list(self.destination):
            personalization.add_to(Email(to_email))
            mail.add_personalization(personalization)

        # add cc (if any)
        if self.cc:
            for cc_email in self._convert_var_type_to_list(self.cc):
                personalization.add_cc(Email(cc_email))
                mail.add_personalization(personalization)

        # add bcc (if any)
        if self.bcc:
            for bcc_email in self._convert_var_type_to_list(self.bcc):
                personalization.add_bcc(Email(bcc_email))
                mail.add_personalization(personalization)

        # add content of email
        if self.body:
            mail.add_content(Content('text/plain', self.body))
        if self.html_message:
            mail.add_content(Content('text/html', self.html_message))

        # add attachments
        if self.attachment:
            mail.add_attachment(self.attachment)

        return mail.get()

    def notify(self):
        """
        """
        sg = self._make_connection()
        data = self._prepare_email_message()

        try:
            return sg.client.mail.send.post(request_body=data)
        except Exception as e:
            return e

RegisterProvider = SendGridProvider
