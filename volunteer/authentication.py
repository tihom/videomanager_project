from django.contrib.auth.models import User

from rest_framework import authentication
# import only works iif glcoud and appengine CLIs are installed
try:
	from google.appengine.api import users as google_users_api
except ImportError:
	google_users_api = None

def google_auth():
	if google_users_api is None:
		return "Google auth api not in path"
	
	user = google_user()
	if user:
		nickname = user.nickname()
		logout_url = google_users_api.create_logout_url('/_/')
		greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
			nickname, logout_url)
	else:
		try:
			login_url = google_users_api.create_login_url('/_/')
			greeting = '<a href="{}">Sign in</a>'.format(login_url)
		except AssertionError:
			greeting = 'Google auth not working'

	return greeting

def google_user():
	# only works on appengine environmet
	try:
		user = google_users_api.get_current_user()
		return user
	except AssertionError:
		return None


class GoogleAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		if google_users_api is None:
			return None
		user = google_user()
		if not user:
			return None

		user, created = User.objects.get_or_create(username=user.nickname(),
								email=user.email())
		return (user, None)
