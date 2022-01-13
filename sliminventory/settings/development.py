from . base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sliminventory_development',
        'USER': 'sliminventory',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}