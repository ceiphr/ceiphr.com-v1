import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default="password"),
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Security for production server use.

# Sentry error logging sdk

sentry_sdk.init(
    dsn="https://64705ba551e4407cb6cc1cf33e6336d8@sentry.io/1429770",
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
