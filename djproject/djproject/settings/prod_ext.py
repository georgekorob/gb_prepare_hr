from .prod import *

SITE_ID = 1

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '54323',
    }
}
