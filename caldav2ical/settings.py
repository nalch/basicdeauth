import errno
import glob
import json
import os

from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STAGE = os.environ.get('STAGE', 'dev')

# settings up settings pipeline
server_settings = {}
for settings_file in glob.glob(os.path.join(BASE_DIR, 'caldav2ical', 'settings_pipeline', '*.json')):
    with open(settings_file) as config_file:
        tmp = server_settings.copy()
        tmp.update(json.load(config_file))
        server_settings = tmp

# import stage settings
try:
    tmp = server_settings.copy()
    tmp.update(json.load(open(os.path.join(BASE_DIR, 'caldav2ical', 'settings_pipeline', 'stages', STAGE+'.json'))))
    server_settings = tmp
except IOError:
    pass

VAR_PATH = server_settings.get('VAR_PATH', os.path.join(os.sep, 'var', 'local', 'caldav2ical'))
CONF_PATH = server_settings.get('CONF_PATH', os.path.join(os.sep, 'etc', 'local', 'caldav2ical', 'conf'))
LOG_PATH = os.path.join(VAR_PATH, 'logs')

try:
    with open(os.path.join(CONF_PATH, 'secret_key')) as f:
        SECRET_KEY = f.read().strip()
except IOError:
    # dev key, set to real secret key in production (happens during Ansible deployment)
    SECRET_KEY = 'iqm3vsw@-9gva5de%8$04(i(a1&@4$jvedqjt3n7_b7uspv$ih'

# paths
STATIC_ROOT = server_settings.get('STATIC_ROOT', os.path.join('static'))
MEDIA_ROOT = server_settings.get('MEDIA_ROOT', os.path.join('media'))

# server settings
DEBUG = server_settings.get('DEBUG', True)
TEMPLATE_DEBUG = server_settings.get('TEMPLATE_DEBUG', True)
ALLOWED_HOSTS = server_settings.get('ALLOWED_HOSTS', [])


# Application definition
INSTALLED_APPS = (
    'nalch_caldav2ical',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'caldav2ical.urls'

WSGI_APPLICATION = 'caldav2ical.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = server_settings.get('DATABASES', {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
})

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    server_settings.get('LOCALE_PATH', os.path.join(BASE_DIR, 'locale')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

try:
    os.makedirs(LOG_PATH, 0o755)
except OSError as exc:  # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(LOG_PATH):
        pass
    else:
        raise

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH + '/caldav2ical.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
