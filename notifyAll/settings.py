#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.config.settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- notifyAll settings.
"""

import os

SMS = 'sms'
EMAIL = 'email'
PUSH = 'push'

PROVIDER_APP_CLASS_PATH = 'notifyAll.providers.{0}.provider.RegisterProvider'

ALLOWED_SERVICES = (SMS, EMAIL, PUSH)

# ----------- Gmail ---------------
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
#
# # ------------ SendGrid -----------
# SENDGRID_EMAIL_BACKEND = "sgbackend.SendGridBackend"
#
#
# PLIVO_AUTH_ID = None
# PLIVO_AUTH_TOKEN = None

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', None)
