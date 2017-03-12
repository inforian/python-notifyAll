from distutils.core import setup
from setuptools import find_packages

setup(
  name='django-notifyAll',
  packages=find_packages(exclude=['example']),
  version='0.1.3',
  description='A lib which you can use for all types of notifications like SMS, Mail, Push.',
  author='Neeraj Dhiman',
  author_email='ndhiman08@gmail.com',
  license='GPL',
  url='https://github.com/inforian/django-notifyAll',
  download_url='https://github.com/inforian/django-notifyAll/archive/0.1.3tar.gz',
  keywords=['notification', 'notify', 'sms', 'email', 'push'],
  classifiers=[],
)