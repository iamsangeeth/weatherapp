from django.db import models
import datetime
from user.models import User

class SearchData(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	data = models.JSONField()
	timestamp = models.DateTimeField(default=datetime.datetime.now())
	locationkey = models.CharField(max_length=255, null=True, blank=True)
