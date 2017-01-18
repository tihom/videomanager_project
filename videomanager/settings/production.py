# -*- coding: utf-8 -*-
from .base import *
from .secrets.production import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# TODO: change this to domain once finalzied
ALLOWED_HOSTS = ["*"]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'volunteer.authentication.GoogleAuthentication',
    ),
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# [START staticurl]
# Fill in your cloud bucket and switch which one of the following 2 lines
# is commented to serve static content from GCS
# STATIC_URL = 'https://storage.googleapis.com/<your-cloud-bucket>/static/'
STATIC_URL = 'http://storage.googleapis.com/videomanager/static/'
# [END staticurl]

STATIC_ROOT = 'static/'