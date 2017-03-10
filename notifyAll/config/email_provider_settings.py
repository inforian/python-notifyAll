#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.config.email_provider_settings
~~~~~~~~~~~~~~

- Email Provider settings and globals.
"""

# ----------- Gmail ---------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'

# ------------ SendGrid -----------
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SENDGRID_API_KEY = None