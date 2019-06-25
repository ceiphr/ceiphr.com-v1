import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', '5432'),
    }
}

# DigitalOcean spaces
# https://www.digitalocean.com/community/tutorials/how-to-set-up-object-storage-with-django

STATIC_URL = "/static/"

# AWS_ACCESS_KEY_ID = os.environ.get('SPACES_ACCESS_KEY', 'spaces-access-key')
# AWS_SECRET_ACCESS_KEY = os.environ.get('SPACES_SECRET_ACCESS_KEY', 'spaces-secret-access-key')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME', 'storage-bucket-name')
# AWS_S3_ENDPOINT_URL = 'https://sfo2.digitaloceanspaces.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'

# STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

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
