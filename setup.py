from distutils.core import setup
from setuptools import find_packages

setup(
  name='python-notifyAll',
  packages=find_packages(exclude=['example']),
  version='0.4',
  description='A library which you can use for all types of notifications like SMS, Mail, Push.',
  author='Neeraj Dhiman',
  author_email='ndhiman08@gmail.com',
  license='GPL',
  url='https://github.com/inforian/python-notifyAll',
  download_url='https://github.com/inforian/python-notifyAll/archive/v0.4.tar.gz',
  keywords=['notification', 'notify', 'sms', 'email', 'push'],
  classifiers=[],
)
