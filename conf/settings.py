INSTALLED_APPS += [
    'uw_person_client',
]

MIGRATION_MODULES = {
    'uw_person_client': 'uw_person_client.test_migrations',
}
