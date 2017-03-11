# django-notifyAll
A lib which you can use for all types of notifications like SMS, Mail, Push.

## Why?

Every application today is dependent on sending out some form of notification - SMS, email or Push.
There is no single interface available to manage either the notification type or the notification service provider.

For SMS
- Plivo
- Twilio
both have their own SDK and API

For Push
- Apple Push
- Android Push
both have their own SDK and API (though Firebase could be used as a single interface)

For Email - The same problem.


## What?

This library aims to provide a uniform interface to all the developers to use any notification mechanism, from any service provider.


### How?

Work in progress, the basic idea is to follow the lead of - django-allauth


### ToDo

- [ ] Notification Provider Base Class
- [ ] Notification SMS Provider Base Class
- [ ] Notification Email Provider Base Class
- [ ] Notification Push Provider Base Class
- [ ] Notification SMS Service Provider - Plivo
- [ ] Notification Email Service Provider - Twilio
- [ ] Notification Email Service Provider - Gmail
- [ ] Notification Email Service Provider - SebdGrid
- [ ] Notification Push Service Provider - ios / APNS
- [ ] Notification Push Service Provider - android
- [ ] Async Notifications - Celery Integration
- [ ] Notifications Reports
- [ ] Notification Push Service Provider - OneSignal
- [ ] Notification Push Service Provider - AirBop