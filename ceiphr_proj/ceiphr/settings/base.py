import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY', default=os.urandom(32))

DEBUG = int(os.getenv('DEBUG', default=1))

ADMIN_ENABLED = int(os.getenv('ADMIN_ENABLED', default=1))

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='127.0.0.1,0.0.0.0').split(',')

# Generic Settings

APPEND_SLASH = True

HTML_MINIFY = True

OTP_TOTP_ISSUER = "Ceiphr"

# Content Security Policy

# CSP_INCLUDE_NONCE_IN = ["script-src"]

# CSP_IMG_SRC = (
#     "'self'",
#     "https://*.ceiphr.com",
#     "https://*.buysellads.net",
#     "https://ad.doubleclick.net",
# )

# CSP_STYLE_SRC = "'self' 'unsafe-inline'"

# CSP_SCRIPT_SRC = (
#     "'self'",
#     "https://*.ceiphr.com",
#     "https://*.carbonads.com",
#     "https://*.carbonads.net",
#     "https://cdnjs.cloudflare.com",
#     "https://sentry.io",
# )

# CSP_FONT_SRC = ("'self' data:", "https://cdnjs.cloudflare.com")

# CSP_FRAME_SRC = ("'self'",)

# CSP_CONNECT_SRC = ("'self'",)

# CSP_OBJECT_SRC = ("'none'",)

# CSP_BASE_URI = ("'none'",)

# CSP_FRAME_ANCESTORS = ("'none'",)

# CSP_FORM_ACTION = "'self'"

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django_otp",
    "django_otp.plugins.otp_totp",
    "django_otp.plugins.otp_hotp",
    "django_otp.plugins.otp_static",
    # "coverage",
    "sorl.thumbnail",
    "compressor",
    "portfolio",
    "blog",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # "csp.middleware.CSPMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

ROOT_URLCONF = "ceiphr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "ceiphr.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME":
     "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},

    {"NAME":
     "django.contrib.auth.password_validation.MinimumLengthValidator"},

    {"NAME":
     "django.contrib.auth.password_validation.CommonPasswordValidator"},

    {"NAME":
     "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, "assets"),)

STATIC_ROOT = os.path.join(BASE_DIR, "static")

COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/media/"
