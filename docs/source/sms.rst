SMS Providers
=============

- Notification Type for all SMS Provider is ``sms``

 .. code-block:: python

    notification_type = 'sms'

> Plivo
-------

**Requirement**
    - you need to install python `plivo`_ package to use this provider.

    .. code-block:: python

        pip install plivo


- Provider Type for all Plivo Provider is ``plivo``

 .. code-block:: python

    provider = 'plivo'

- When you register at `Plivo` it will give you two keys which you need to configure in your Django Project.


PLIVO_AUTH_ID
+++++++++++++

PLIVO_AUTH_TOKEN
++++++++++++++++


> Twilio
--------


**Requirement**
    - you need to install python `twilio`_ package to use this provider.

    .. code-block:: python

        pip install twilio

- Provider Type for all Twilio Provider is ``twilio``

 .. code-block:: python

    provider = 'twilio'

- When you register at `Twilio` it will give you two keys which you need to configure in your Django Project.


TWILIO_ACCOUNT_SID
++++++++++++++++++

TWILIO_AUTH_TOKEN
+++++++++++++++++


.. _plivo: https://github.com/plivo/plivo-python
.. _twilio:  https://github.com/twilio/twilio-python