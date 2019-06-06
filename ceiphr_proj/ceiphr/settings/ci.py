from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'circle_test',
        'USER': 'root',
        # 'PASSWORD': env_config.postgres_PW,
        'HOST': 'localhost',
        'PORT': '',
    }
}