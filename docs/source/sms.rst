SMS Providers
=============

- Notification Type for all SMS Provider is ``sms``

 .. code-block:: python

    notification_type = 'sms'

- Configuration settings can be passed as function arguments as well as in `Environment Variable`. The main AIM is to provide all
	possible flexibility to user to use Any `Provider` with any configuration.


> Plivo
-------

**Requirement**
    - you need to install python `plivo`_ package to use this provider.

    .. code-block:: python

        pip install plivo


- Provider Type for all Plivo Provider is ``plivo``

 .. code-block:: python

    provider = 'plivo'

- When you register at `Plivo` it will give you two keys which you need to configure in your Project.

**As Environment Variable :**

PLIVO_AUTH_ID
+++++++++++++

PLIVO_AUTH_TOKEN
++++++++++++++++

**As Function Arguments:**

- `PLIVO_AUTH_ID` as `auth_id`
- `PLIVO_AUTH_TOKEN` as `auth_token`


**Example Usage** :

 .. code-block:: python

    from notifyAll.services import notifier


    def notify():
        """
        """
        data = {
            'source': '<source>',
            'destination': '<destination>',
            'notification_type': 'sms',
            'provider': 'plivo',
            'context': {
                'body': 'test message'
            },
        }

        notification = notifier.Notifier(**data)

        return notification.notify(auth_id='<plivo_auth_id>', auth_token='<plivo_auth_token>')


> Twilio
--------


**Requirement**
    - you need to install python `twilio`_ package to use this provider.

    .. code-block:: python

        pip install twilio

- Provider Type for all Twilio Provider is ``twilio``

 .. code-block:: python

    provider = 'twilio'

- When you register at `Twilio` it will give you two keys which you need to configure in your Project.

**As Environment Variable :**

TWILIO_ACCOUNT_SID
++++++++++++++++++

TWILIO_AUTH_TOKEN
+++++++++++++++++

**As Function Arguments:**

- `TWILIO_ACCOUNT_SID` as `account_sid`
- `TWILIO_AUTH_TOKEN` as `auth_token`


- Usage is same as shown in `Plivo` provider example

.. _plivo: https://github.com/plivo/plivo-python
.. _twilio:  https://github.com/twilio/twilio-python