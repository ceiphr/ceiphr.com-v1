import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import ceiphr.settings.env_config as env_config
from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ceiphrcom',
#         'USER': 'ceiphrcom',
#         'PASSWORD': env_config.postgres_PW,
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Security for production server use.

# Sentry error logging sdk

sentry_sdk.init(
    dsn=env_config.sentry_dsn,
    integrations=[DjangoIntegration()]
)

# Production config security hardening

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

X_FRAME_OPTIONS = 'DENY'

# One year strict transport security expiration

SECURE_HSTS_SECONDS = 31536000
