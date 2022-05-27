from .common import *

SECRET_KEY = 'django-insecure-t$h2ut#i(r!o0&b(+(9aldj1#iukoop%(ru#8d1%)99(5q8j(w'

ALLOWED_HOSTS = ['*']

DEFAULT_FROM_EMAIL = os.environ.get('EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'assets/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'database': os.environ.get('DB_NAME'),
            'user': os.environ.get('DB_USER'),
            'password': os.environ.get('DB_PASSWORD','')        
        },
    }
}