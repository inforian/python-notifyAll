Welcome to django-notifyAll's documentation !
=============================================

A library which can be used for all types of notifications like SMS, Mail, Push.

- Supports Python 3+

**Documentation :** https://django-notifyall.readthedocs.io/en/latest/index.html

Why?
====

Every application today is dependent on sending out some form of notification - SMS, email or Push.
There is no single interface available to manage either the notification type or the notification service provider.

For SMS
+++++++
- Plivo
- Twilio

both have their own SDK and API

For Push
++++++++
- Apple Push
- Android Push

both have their own SDK and API (though Firebase could be used as a single interface)

For Email
+++++++++
- The same problem.

What?
========

This library aims to provide a uniform interface to all the developers to use any notification mechanism, from any service provider.


How?
====

Work in progress, the basic idea is to follow the lead of `django-allauth`_.


Contents
========

.. toctree::
    :titlesonly:
    :maxdepth: 2

    overview
    installation
    providers
    example
    contribute
    license



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _django-allauth: https://django-allauth.readthedocs.io/en/latest/index.html
