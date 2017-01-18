# -*- coding: utf-8 -*-
from .base import *
from .secrets.testing import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'volunteer.authentication.GoogleAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}