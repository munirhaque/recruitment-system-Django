from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from exams.models import Exam, ExamQuestionTopic
from examinees.models import Examinee, ExamineeExam
from questions.models import Question, Options
# Create your views here.

def index(request):
	return render(request, 'examinee_login.html')

def user_login(request):
	if request.method == 'POST':
		examinee_name = request.POST['name']
		email=request.POST['email']
		exams = Exam.objects.filter(start_date__gt=date.today())
		examinee_data = {'name':examinee_name, 'email':email, 'exams':exams}
		return render(request, 'examinees/examinees-available-exams.html', context=examinee_data)
		#return HttpResponse(examinee_name + "<br/>" + email)

def start_exam(request, exam_id, name, email):
	Examinee.objects.create(name=name, email=email)

	examinee = Examinee.objects.latest('id')
	ExamineeExam.objects.create(examinee_id = examinee.id, exam_id=exam_id)
	
	exam = Exam.objects.get(id=exam_id)
	#time_per_question = exam.time_duration / exam.number_of_question
	
	exam_questions = ExamQuestionTopic.objects.filter(exam_id=exam_id).first()
	exam_question_id = exam_questions.id

	question = Question.objects.get(id=exam_questions.question_id)

	options= Options.objects.filter(question_id=question.id)
	counter = 1
	exam_data = {'exam_id':exam_id, 'examinee_id':examinee.id, 
				 'question':question,'options':options, 'exam_question_id':exam_question_id,
				 'counter':counter
				 }

	return render(request, 'examinees/demo.html', context=exam_data)
	#for q in questions:
	#return HttpResponse(options.option)
	#return HttpResponse(str(exam_id) + "<br/>" + name + "<br/>" + email)
		# exam_data = {'exam_id':exam_id, 'name':name, 'email':email}
		# return render(request, 'examinees/examinees-rules.html', context=exam_data)

def submit_answer(request, exam_id, examinee_id, question_id, counter ):

	start = counter
	end = counter + 1
	answer = request.POST['answer']
	ExamineeExam.objects.create(examinee_id = examinee_id, exam_id=exam_id, 
								question_id =question_id, answer_id = answer)

	total_questions = ExamQuestionTopic.objects.filter(exam_id=exam_id).count()
	if counter < total_questions:
		exam_questions = ExamQuestionTopic.objects.filter(exam_id=exam_id)[start:end].get()
	elif counter >= total_questions:
		return render(request, 'examinees/examinee-exam-end.html')

	question = Question.objects.get(id=exam_questions.question_id) 
	options= Options.objects.filter(question_id=question.id)
	counter = end
	exam_data = {'exam_id':exam_id, 'examinee_id':examinee_id, 
				 'question':question,'options':options,'counter':counter
				 }
	return render(request, 'examinees/demo.html', context=exam_data)
	
		#return HttpResponse(answer)