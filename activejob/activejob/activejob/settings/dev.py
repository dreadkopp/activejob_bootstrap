from .base import *


SECRET_KEY = '@(m2uopcek&#ct6*uf8=n!+@i$3r*i9rq3th52#=voexp-mm@2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'yoshi.dynu.com',
    'localhost',
]

INSTALLED_APPS += [
    'django.contrib.admin',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
