from django.db import models
from questions.models import Question
from topics.models import Topic

class Exam(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	number_of_question = models.IntegerField()
	time_duration = models.IntegerField()

class ExamQuestionTopic(models.Model):
	id = models.AutoField(primary_key = True)
	# exam_id = models.IntegerField()
	# question_id = models.IntegerField()
	# topic_id = models.IntegerField() 
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)