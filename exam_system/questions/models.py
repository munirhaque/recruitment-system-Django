from django.db import models
from topics.models import Topic

# Create your models here.
class Question(models.Model):
	id = models.AutoField(primary_key = True)
	question = models.TextField()
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	

class Options(models.Model):
	id = models.AutoField(primary_key = True)
	option = models.TextField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	is_answer = models.SmallIntegerField(null = True)