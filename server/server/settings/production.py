from . import *

SECRET_KEY = 'django-insecure-t$h2ut#i(r!o0&b(+(9aldj1#iukoop%(ru#8d1%)99(5q8j(w'

ALLOWED_HOSTS = ['*']

DEFAULT_FROM_EMAIL = env('EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR/'server/static',
]
STATIC_ROOT = BASE_DIR/'assets/static'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'assets/media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'database': env('DB_NAME'),
            'user': env('DB_USER'),
            'password': env('DB_PASSWORD')        
        },
    }
}