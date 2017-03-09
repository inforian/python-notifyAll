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

# local

# own app


class Provider(object):
    """
    """
    id = None

    def get_config(self):
        """

        :return: provider configuration settings
        """
        pass

    def notify(self):
        """send notification to respective recipient

        """
        pass
