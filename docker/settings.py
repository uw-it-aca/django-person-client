from .base_settings import *
import os

INSTALLED_APPS += [
    'uw_person_client',
    'django.contrib.postgres',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'uw_person': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'OPTIONS': {
            'pool': {'min_size': 1, 'max_size': 2},
        },
    },
}

MIGRATION_MODULES = {
    'uw_person_client': 'uw_person_client.test_migrations',
}

FIXTURE_DIRS = ['uw_person_client/fixtures']

DATABASE_ROUTERS = ["uw_person_client.routers.UWPersonRouter"]
