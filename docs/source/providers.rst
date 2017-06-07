Providers
=========

Most of the Providers needs you to register on their site and get some kind of token/secret in order to use their services.

I'll try to explain what settings you need in order to user Any below providers.

.. toctree::
   :maxdepth: 2

   email
   sms

**Note :** Providers can be managed in two ways using `django settings` or as `function arguments`.
See respective Providers docs for more info

Add providers
=============

If you want to contribute to this repo and wish to add more providers just follow below instructions:

- All providers (provider apps) comes under this folder ``notifyAll/providers``.
- Naming convention of provider app and class is as follows :

   - Class `id` and provider `app_name` must be same

   e.g., For `Gmail` provider , `id` & `app_name` both are same i.e., `gmail`

- If your provider require some settings from user then add them here too ``notifyAll/providers/provider_config.py``
- Also update `Provider`_ documentation for your provider (Update respective doc only means email,sms have their own documentation).


- Update service configuration file to add your provider in ``ALLOWED_SERVICES`` at ``notifyAll/services/service_config.py``
  so that your provider can be enabled for outer world.


.. _Provider: https://django-allauth.readthedocs.io/en/latest/providers.html
