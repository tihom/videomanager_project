from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Volunteer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	leader = models.ForeignKey(User, related_name="team", blank=True, null=True, default=None)
	phone_number = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return self.user.username
