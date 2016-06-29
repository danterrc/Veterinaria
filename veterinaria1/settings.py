"""
Django settings for veterinaria project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ii3x-k^f_2-=fbng(x85z1%=baq7rhlj$n#0_4nspp6gx$goi'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['localhost','127.0.0.1']

from django_apps import home, core, inventario, persona, compras, ventas, clinica
# Application definition

INSTALLED_APPS = [
    'django_apps.home',
    'django_apps.core',
    'django_apps.inventario',
    'django_apps.persona',
    'django_apps.compras',
    'django_apps.ventas',
    'django_apps.clinica',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_countries',
    'jquery',
    'djangoformsetjs',
    'django_extensions',
    'django_db_signals',
    # 'crispy_forms',
    # 'extra_views',
    # 'linguist',
    # 'rosetta',
    'wkhtmltopdf',
    # 'ajax_select',
    # 'social.apps.django_app.default',
]

# WKHTMLTOPDF_CMD = '/path/to/my/wkhtmltopdf'
# WKHTMLTOPDF_CMD = '/home/dante/.virtualenvs/django-1.9/local/lib/python2.7/site-packages/wkhtmltopdf/'
# WKHTMLTOPDF_CMD = '/usr/local/bin/wkhtmltopdf'
# WKHTMLTOPDF_CMD_OPTIONS = 'some_option_here'

# CRISPY_TEMPLATE_PACK = 'uni_form'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
]
# GEOIP_DATABASE = '/path/to/your/geoip/database/GeoLiteCity.dat'
# GEOIPV6_DATABASE = '/path/to/your/geoip/database/GeoLiteCityv6.dat'

ROOT_URLCONF = 'veterinaria1.urls'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # 'social.apps.django_app.context_processors.backends',
                # 'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]


# AUTHENTICATION_BACKENDS = [
#     'social.backends.open_id.OpenIdAuth',
#     'social.backends.twitter.TwitterOAuth',
#     'social.backends.facebook.FacebookOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# ]

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
WSGI_APPLICATION = 'veterinaria1.wsgi.application'


# GRAPH_MODELS = {
#   'all_applications': True,
#   'group_models': True,
# }
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DATABASESm = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'veterinaria',
        'USER': 'dante',
        'PASSWORD': 'elmejor56',
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'home.Empleado'
# AUTH_PROFILE_MODULE = 'persona.PerfilEmpleado'
# ACCOUNT_ACTIVATION_DAYS = 7
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('ja', _('Japanese')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese')),
    ('fr', _('French')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('es-ar', _('Argentinian Spanish')),
    ('es-pe', _('Spanish')),
    ('pt', _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),
    ('it', _('Italian')),
    ('he', _('Hebrew')),
    ('ko', _('Korean')),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/'
# ADMIN_MEDIA_PREFIX = '/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'dante.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'dantespeed14@gmail.com'  # cambie por el suyo
# EMAIL_HOST_PASSWORD = 'elmejor56'  # cambie por el suyo
# DEFAULT_FROM_EMAIL = 'dantespeed14@gmail.com'  # cambie por el suyo
# AJAX_LOOKUP_CHANNELS = {
#     'product': {
#         'model': 'django_apps.compras.OrdenCompra',
#         'search_field': 'proveedor',
#     }
# }

WKHTMLTOPDF_CMD = '/usr/bin/wkhtmltopdf'
WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': True,
}
