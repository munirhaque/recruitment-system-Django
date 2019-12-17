from django.db import models

# Create your models here.

class Examinee(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)

class ExamineeExam(models.Model):
	id = models.AutoField(primary_key=True)
	examinee = models.ForeignKey(Examinee, on_delete=models.CASCADE)
	exam_id = models.IntegerField(null=True)
	question_id = models.IntegerField(null=True)
	answer_id = models.IntegerField(null=True)