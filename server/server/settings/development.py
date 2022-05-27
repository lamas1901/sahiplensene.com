from .common import *

SECRET_KEY = 'secret-key'

ALLOWED_HOSTS = ['*']

DEFAULT_FROM_EMAIL = os.environ.get('EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR/'server/static',
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'assets/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'assets/tmp/db.sqlite3',
    }
}