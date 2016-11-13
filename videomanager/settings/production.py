# -*- coding: utf-8 -*-
from .base import *
from .secrets.production import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# TODO: change this to domain once finalzied
ALLOWED_HOSTS = ["*"]