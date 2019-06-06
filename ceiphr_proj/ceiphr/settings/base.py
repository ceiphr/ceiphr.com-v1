import os

import ceiphr.settings.env_config as env_config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env_config.secret_key

ADMIN_ENABLED = True

ALLOWED_HOSTS = ['ceiphr.com', 'staging.ceiphr.com', '127.0.0.1', '104.248.5.8']

# Generic Settings

APPEND_SLASH = True

OTP_TOTP_ISSUER = 'Ceiphr'

HTML_MINIFY = True

# Content Security Policy

CSP_INCLUDE_NONCE_IN=['script-src']

CSP_IMG_SRC = ("'self'", 'https://*.ceiphr.com', 'https://*.buysellads.net', 'https://ad.doubleclick.net', 'https://img.shields.io')

CSP_STYLE_SRC = ("'self' 'unsafe-inline'")

CSP_SCRIPT_SRC = ("'self'", 'https://*.ceiphr.com', 'https://*.carbonads.com', 'https://*.carbonads.net', 'https://cdnjs.cloudflare.com', 'https://sentry.io')

CSP_FONT_SRC = ("'self' data:", 'https://cdnjs.cloudflare.com')

CSP_FRAME_SRC = ("'self'", )

CSP_CONNECT_SRC = ("'self'", )

CSP_OBJECT_SRC = ("'none'", )

CSP_BASE_URI = ("'none'", )

CSP_FRAME_ANCESTORS = ("'none'", )

CSP_FORM_ACTION = ("'self'")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_hotp',
    'django_otp.plugins.otp_static',

    'coverage',
    'sorl.thumbnail',
    'pipeline',
    
    'portfolio',
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

ROOT_URLCONF = 'ceiphr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ceiphr.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'assets'),)

STATIC_URL = '/static/'

# Pipeline - process and compress assets for optimized use

PIPELINE = {
    # Convert stylesheet assets into post-processed static content
    'STYLESHEETS': {
        'feed-mobile': {
            'source_filenames': (
                'sass/feed-mobile.scss',
                'sass/rain.scss',
            ),
            'output_filename':
            'css/feed-mobile.css',
            'extra_context': {
                'media': 'screen and (max-width: 769px)',
            },
        },
        'feed-desktop': {
            'source_filenames': (
                'sass/feed-desktop.scss',
                'sass/rain.scss',
            ),
            'output_filename':
            'css/feed-desktop.css',
            'extra_context': {
                'media': 'screen and (min-width: 769px)',
            },
        },
        'article-mobile': {
            'source_filenames': (
                'sass/article-mobile.scss',
                'sass/highlight.scss',
            ),
            'output_filename':
            'css/article-mobile.css',
            'extra_context': {
                'media': 'screen and (max-width: 1024px)',
            },
        },
        'article-desktop': {
            'source_filenames': (
                'sass/article-desktop.scss',
                'sass/highlight.scss',
            ),
            'output_filename':
            'css/article-desktop.css',
            'extra_context': {
                'media': 'screen and (min-width: 1024px)',
            },
        },
    },
    # Compress javascript assets
    'JAVASCRIPT': {
        'onload': {
            'source_filenames': (
                'node_modules/lazysizes/lazysizes.js',
                'node_modules/lazysizes/plugins/blur-up/ls.blur-up.js',
            ),
            'output_filename':
            'js/onload.js',
            'extra_context': {
                'defer': True,
            },
        },  
        'nav': {
            'source_filenames': (
                'js/nav.js',
            ),
            'output_filename':
            'js/mobile-nav.js',
            'extra_context': {
                'defer': True,
            },
        },         
    },
}

# Sass compiler for coverting scss files to post-processed css

PIPELINE['COMPILERS'] = (
    'pipeline.compilers.sass.SASSCompiler',
)

# Custom css and js compressors

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.yuglify.YuglifyCompressor'

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
