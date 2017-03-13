#!/usr/bin/python
# -*- coding: utf-8 -*-

from notifyAll.services import notifier


def notify(**kwargs):
    """
    """
    notification = notifier.Notifier(
        source=kwargs.get('source'),
        destination=kwargs.get('destination'),
        notification_type=kwargs.get('notification_type'),
        provider=kwargs.get('provider'),
        context=kwargs.get('context')
    )

    return notification.notify()
