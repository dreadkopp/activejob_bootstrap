from .base import *


SECRET_KEY = os.environ.get("SECRET_KEY", "")

ALLOWED_HOSTS = [
    'activ-job.com',
    'www.activ-job.com',
    "localhost",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "activjob",
    }
}
