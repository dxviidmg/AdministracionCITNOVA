from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	position = models.CharField(max_length=30)
	phone = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return '{} {}'.format(self.user.first_name, self.user.last_name)