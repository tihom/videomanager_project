## Videomanager
Web project to manage educational videos. Applications include:
- Translation of Khan Academy videos to other lanaguages.

#### Getting Started
Add secret config files in settings/secrets folder for each enviroment e.g. development.py
Config template and notes on how to generate them are in settings/secrets/__init__.py.

To run in a particular enviroment set the following (can also be done in postactivate of a virtualenv):
DJANGO_SETTINGS_MODULE="videomanager.settings.development"

#### References
For intial set up (virtualenv, python, folder structure) refer: 
http://www.marinamele.com/taskbuster-django-tutorial/taskbuster-working-environment-and-start-django-project

Production Setup:
http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
