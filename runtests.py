#!/usr/bin/env python
import sys

from django import setup
from django.conf import settings
from django.test.runner import DiscoverRunner as TestRunner

SETTINGS = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev.db',
        },
        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'dpaste',
        #     'USER': 'root',
        #     'PASSWORD': '',
        # }
    },
    'MEDIA_ROOT': '/tmp/',
    'ROOT_URLCONF': 'attachments.tests.testapp.urls',
    'INSTALLED_APPS': [
        'attachments',
        'attachments.tests.testapp',

        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',

    ],
    'MIDDLEWARE_CLASSES': (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
    ),
}

def runtests(*test_args):
    # Setup settings
    if not settings.configured:
        settings.configure(**SETTINGS)

    setup()

    test_runner = TestRunner(verbosity=1)
    failures = test_runner.run_tests(['attachments'])
    if failures:
        sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
