from django.contrib.auth.models import User

from rest_framework.authentication import BaseAuthentication
# import only works iif glcoud and appengine CLIs are installed
try:
	from google.appengine.api import users as google_users_api
except ImportError:
	google_users_api = None

class GoogleAuthException(Exception):
    pass

class GoogleAuthentication(BaseAuthentication):

	def is_valid(self):
		if google_users_api is None:
			return False
		try:
			user = google_users_api.get_current_user()
			return True
		except AssertionError:
			return False

	def auth_greeting(self, redirect_path):
		if google_users_api is None:
			raise GoogleAuthException("Google auth api not in path")
		
		user = self.get_user()
		if user:
			nickname = user.nickname()
			logout_url = google_users_api.create_logout_url(redirect_path)
			greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
				nickname, logout_url)
		else:
			try:
				login_url = google_users_api.create_login_url(redirect_path)
				greeting = '<a href="{}">Sign in</a>'.format(login_url)
			except AssertionError:
				raise GoogleAuthException('Google auth not working')

		return greeting

	def get_user(self):
		# only works on appengine environmet
		try:
			user = google_users_api.get_current_user()
			return user
		except AssertionError:
			return None

	def authenticate(self, request):
		if google_users_api is None:
			return None
		
		user = self.get_user()
		if not user:
			return None

		user, created = User.objects.get_or_create(username=user.nickname(),
								email=user.email())
		return (user, None)
