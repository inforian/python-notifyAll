#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.providers.provider_config
~~~~~~~~~~~~~~

- This file contains the general configuration settings of All Provider.
"""

# future
from __future__ import unicode_literals

# 3rd party

# Django
from django.conf import settings

# local

# own app


EMAIL_HOST = getattr(settings, 'EMAIL_HOST', '')
EMAIL_HOST_PASSWORD = getattr(settings, 'EMAIL_HOST_PASSWORD', '')
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER', '')
EMAIL_PORT = getattr(settings, 'EMAIL_PORT', 587)
DEFAULT_FROM_EMAIL = getattr(settings, 'DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
