from .base import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci_test',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}
