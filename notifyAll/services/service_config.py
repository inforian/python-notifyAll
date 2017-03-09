#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- notifyAll.services.service_config
~~~~~~~~~~~~~~

- This file contains the general settings of services this library will provide
"""

SMS = 'sms'
EMAIL = 'email'
PUSH = 'push'

PROVIDER_APP_CLASS_PATH = 'notifyAll.providers.{0}.provider.RegisterProvider'

ALLOWED_SERVICES = (SMS, EMAIL, PUSH)
