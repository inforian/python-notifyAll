Example
=======

Example project can be find out `here`_

- Its a Django project.Follow below instructions to set up this project.

- Download above example project (if you set up virtual; env then that will good.)
- Go inside example directory from terminal.
- Install all requirements using below command :

 .. code-block:: python

    pip install -r requirements.txt

- Add settings for provider you want to test in your settings.py , For What settings you need to put in settings.py
  read `Provider`_ page.

- run local server as

 .. code-block:: python

    python manage.py runserver

- Access server in browser using ``http://localhost:8000`` . you will see a page with forms for every notification,
  Fill any one form and click on send, you will see a success message on successful notification send or an error
  message (if any)

**Note :** If you face any issue raise an issue on our `github`_ repo



.. _here:  https://github.com/inforian/django-notifyAll/tree/master/example
.. _Provider: https://django-allauth.readthedocs.io/en/latest/Providers.html
.. _github: https://github.com/inforian/django-notifyAll
