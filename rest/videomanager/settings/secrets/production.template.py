import os

'''
### To generate a new secret key:
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
get_random_string(50, chars)
'''

SECRET_KEY = raise Exception("Add Secret Key")


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# [START db_setup]
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/vetrivel-foundation:us-central1:videomanager2',
            'NAME': 'videomanager',
            'USER': raise Exception("Need username"),
            'PASSWORD': raise Exception("Need password"),
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ ./cloud_sql_proxy \
    #        -instances=vetrivel-foundation:us-central1:videomanager2=tcp:3306 \
    #        -credential_file=************.json
    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'videomanager',
            'USER': raise Exception("Need username"),
            'PASSWORD': raise Exception("Need password"),
        }
    }
# [END db_setup]