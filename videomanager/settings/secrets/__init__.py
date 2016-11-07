# add secret settings per environment e.g. development.py in this folder
# template:
'''
### To generate a new secret key:
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
get_random_string(50, chars)
###
SECRET_KEY = '...'


'''
