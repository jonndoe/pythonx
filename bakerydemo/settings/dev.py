from .base import *  # noqa: F403, F401
import os

DEBUG = True

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.yandex.ru'
#EMAIL_HOST_USER = 'pythonix@yandex.ru'
#EMAIL_HOST_PASSWORD = 'password'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#SERVER_EMAIL = EMAIL_HOST_USER
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'
