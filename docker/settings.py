from .base_settings import *

INSTALLED_APPS += [
    'uw_person_client',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'db',
        'PORT': '5432',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    },
}

MIGRATION_MODULES = {
    'uw_person_client': 'uw_person_client.test_migrations',
}

FIXTURE_DIRS = ['uw_person_client/fixtures']
