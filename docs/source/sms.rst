SMS Providers
=============

- Notification Type for all SMS Provider is ``sms``

 .. code-block:: python

    notification_type = 'sms'

- General Settings you need to configure in Django Project when using any email providers are mentioned below :

- Some settings can be passed as function arguments as well as in `Django settings`. The main AIM is to provide all
	possible flexibility to user to use Any `Provider` with any configuration.

- If we Add settings in `Django settings` then in entire project those settings will be used But if you want every
	notification use different provider configuration then that is also possible here.


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

**As Django settings :**

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

- When you register at `Twilio` it will give you two keys which you need to configure in your Django Project.

**As Django settings :**

TWILIO_ACCOUNT_SID
++++++++++++++++++

TWILIO_AUTH_TOKEN
+++++++++++++++++

**As Function Arguments:**

- `TWILIO_ACCOUNT_SID` as `account_sid`
- `TWILIO_AUTH_TOKEN` as `auth_token`


- Usage is same as shown in `Plivo` provider example

> Msg91
-------


**Requirement**
    - you need to install python `requests`_ package to use this provider.

    .. code-block:: python

        pip install requests

- Provider Type for all Twilio Provider is ``msg91``

 .. code-block:: python

    provider = 'msg91'

- When you register at `Msg91` it will give you one key which you need to configure in your Project.

**As Django settings :**

MSG91_AUTHKEY
+++++++++++++

**Optional Settings**

MSG91_PROMOTIONAL_ROUTE
+++++++++++++++++++++++

- Default value is `1`

MSG91_TRANSACTIONAL_ROUTE
+++++++++++++++++++++++++

- Default value is `4`


**As Function Arguments:**

- `MSG91_AUTHKEY` as `auth_key`


- Usage is same as shown in `Plivo` provider example


.. _plivo: https://github.com/plivo/plivo-python
.. _twilio:  https://github.com/twilio/twilio-python
.. _requests: http://docs.python-requests.org/en/master/