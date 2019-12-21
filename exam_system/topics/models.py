from django.db import models


class Topic(models.Model):
	id = models.AutoField(primary_key = True)
	topic_name = models.CharField(max_length = 100, unique=True)

