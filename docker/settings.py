from .base_settings import *
import os

INSTALLED_APPS += [
    'uw_person_client',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'testdb',
        'USER': 'tester',
        'PASSWORD': 'tester',
    },
}

MIGRATION_MODULES = {
    'uw_person_client': 'uw_person_client.test_migrations',
}
