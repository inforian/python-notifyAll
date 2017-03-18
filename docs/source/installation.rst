Installation and Usage
======================

Installation
------------

Django
++++++

Python package:

 .. code-block:: python

    pip install django-notifyAll

settings.py

- Add ``notifyAll`` in your ``INSTALLED_APPS``


Further settings depends on the Provider you Choose. Visit `Provider`_ page for that.


Usage
-----

- import notifier from notifyAll services as :

 .. code-block:: python

    from notifyAll.services import notifier

- Then call `notifier.Notifier()`, there are some required params which are as follows:


source
++++++
    This signifies who wants to send notification.

destination
+++++++++++
    To whom you want to send notification.

notification_type
+++++++++++++++++
    This signifies the Notification type available options are  ``sms, email or push``.

    Note : `push` Notification support is not available yet,

provider
++++++++
    Type of Provider e.g., ``plivo, twilio, gmail etc``, for more info visit `Provider`_ page for that.

context
+++++++
    All other information will come under context, it is of type ``dict``. e.g., notification body, cc, bcc or attachement
    in case of email.

    - Possible keys of context :

    **body :**
        Body of Notification.

    **cc :**
        For email provider only.

    **bcc :**
        For email provider only.

    **attachment :**
        For email provider only.

    **html_message :**
        For email provider only. If you want to send message including **HTML** then you need to send your notification body
        in the above key.


**Example Usage** :

 .. code-block:: python

    from notifyAll.services import notifier


    def notify():
        """
        """
        context = {
            'subject': 'subject'
            'body': 'body'
            'html_message': '<h1>html message</h1>'
        }

        data = {
            'source': 'admin@example.com',
            'destination': 'me@example.com',
            'notification_type': 'email',
            'provider': 'gmail',
            'context': context,
        }

        notification = notifier.Notifier(
            source=data.get('source'),
            destination=data.get('destination'),
            notification_type=data.get('notification_type'),
            provider=data.get('provider'),
            context=data.get('context')
        )

        return notification.notify()

For more information about usage visit our `Example`_ project.

.. _Provider: https://django-allauth.readthedocs.io/en/latest/Providers.html
.. _Example: https://django-allauth.readthedocs.io/en/latest/example.html