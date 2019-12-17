from django.db import models

class Exam(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	number_of_question = models.IntegerField()
	time_duration = models.IntegerField()

class ExamQuestionTopic(models.Model):
	id = models.AutoField(primary_key = True)
	exam_id = models.IntegerField()
	question_id = models.IntegerField()
	topic_id = models.IntegerField() 