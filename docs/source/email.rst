Email Providers
===============

- Notification Type for all Email Provider is ``email``

 .. code-block:: python

    notification_type = 'email'

General Settings you need to configure in Django Project when using any email providers are mentioned below :

> General Settings
------------------

EMAIL_USE_TLS :
+++++++++++++++
    Whether to use a TLS (secure) connection when talking to the **SMTP** server. Default ``True``.

EMAIL_BACKEND :
+++++++++++++++
    The backend to use for sending emails. Default: `django.core.mail.backends.smtp.EmailBackend`.

EMAIL_HOST :
++++++++++++
    The host to use for sending email.

EMAIL_HOST_USER :
+++++++++++++++++
Username to use for the SMTP server defined in `EMAIL_HOST`.

EMAIL_HOST_PASSWORD :
+++++++++++++++++++++
Password to use for the SMTP server defined in `EMAIL_HOST`.

EMAIL_PORT :
++++++++++++
Port to use for the SMTP server defined in `EMAIL_HOST`.

DEFAULT_FROM_EMAIL :
++++++++++++++++++++
Default email address to use for various outgoing emails.

**Note :** Any Provider may need some extra settings (if any) those will be mentioned in respective Provider.


> Gmail
-------

- Provider Type for all Gmail Provider is ``gmail``

 .. code-block:: python

    provider = 'gmail'

- You can use Gmail as your **SMTP** provider an send Emails from Your own Gmail account.
- For this you need below settings to configure in your Django Project.
- Sample settings for Gmail Provider are as follows:

 .. code-block:: python

    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'myuser@gmail.com'  # my gmail username
    EMAIL_HOST_PASSWORD = 'mypassword'  # my gmail password
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

> SendGrid
----------

- Provider Type for all Sendgrid Provider is ``sendgrid``

 .. code-block:: python

    provider = 'sendgrid'

- Use `Sendgrid` as your **SMTP** provider
- You need to register to sendgrid for using their services , from their you will get an

SENDGRID_API_KEY :
++++++++++++++++++
    you sendgrid api_key, it is visible only once, so you need to copy it after craeting.


- Sample settings for SendGrid Provider are as follows:

 .. code-block:: python

    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    SENDGRID_API_KEY = 'my-send-grid-api-key'
    EMAIL_HOST_USER = 'sendgriduser'  # will be provided by sendgrid
    EMAIL_HOST_PASSWORD = 'sendgridpass'  # will be provided by sendgrid
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

