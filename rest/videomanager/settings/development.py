# -*- coding: utf-8 -*-
from .base import *
from .secrets.development import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SITE ROOT PATH
# custom config to host the site on a non-root path
SITE_ROOT_PATH = "rest/"
# url path for static files
# url path for static files
STATIC_URL = '/rest/static/'