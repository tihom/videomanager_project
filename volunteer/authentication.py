from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions


class GoogleAuthentication(authentication.BaseAuthentication):
	def authenticate(self, request):
		# import here only as only works in production
		from google.appengine.api import users

		user = users.get_current_user()
		if not user:
			return None

		user, created = User.objects.get_or_create(username=user.nickname,
								email=user.email)
		return (user, None)
