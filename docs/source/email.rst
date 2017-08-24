Email Providers
===============

- Notification Type for all Email Provider is ``email``

 .. code-block:: python

    notification_type = 'email'

- Configuration Settings can be passed as function arguments as well as `Environment Variable`. The main AIM is to provide all
    possible flexibility to user to use Any `Provider` with any configuration.

**Note :** Any Provider may need some extra settings (if any) those will be mentioned in respective Provider.


> Gmail
-------

- Provider Type for all Gmail Provider is ``gmail``

 .. code-block:: python

    provider = 'gmail'

- You can use Gmail as your **SMTP** provider an send Emails from Your own `Gmail` account.
- For this you need below settings to configure in your Django Project.
- Sample settings for Gmail Provider are as follows:

**As Environment Variable :**

- `GMAIL_USERNAE`
- `GMAIL_PASSWORD`

**As Function Arguments:**

- `GMAIL_USERNAE` as `username`.
- `GMAIL_PASSWORD` as `password`.

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

        notification = notifier.Notifier(**data)

        return notification.notify(username='myuser@gmail.com', password='mypassword')


> SendGrid
----------

- Provider Type for all Sendgrid Provider is ``sendgrid``

 .. code-block:: python

    provider = 'sendgrid'

- Use `Sendgrid` as your **SMTP** provider
- You need to register to sendgrid for using their services , from their you will get an

SENDGRID_API_KEY :
++++++++++++++++++
    you sendgrid api_key, it is visible only once, so you need to copy it after creating.


- Sample settings for SendGrid Provider are as follows:

**As Environment Variable :**

- `SENDGRID_API_KEY`


**As Function Arguments:**

- `SENDGRID_API_KEY` as `sendgrid_api_key`.

- Usage is same as shown in `Gmail` provider example
