#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.gmail.gmail_provider_config
~~~~~~~~~~~~~~

- This file contains the configuration settings of Gmail Provider
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.conf import settings

# local

# own app


EMAIL_USE_TLS = getattr(settings, 'EMAIL_USE_TLS', True)
EMAIL_BACKEND = getattr(settings, 'EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = getattr(settings, 'EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_PASSWORD = getattr(settings, 'EMAIL_HOST_PASSWORD', '')  # my gmail password
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER', '')  # my gmail username
EMAIL_PORT = getattr(settings, 'EMAIL_PORT', 587)
DEFAULT_FROM_EMAIL = getattr(settings, 'EMAIL_HOST', EMAIL_HOST_USER)
