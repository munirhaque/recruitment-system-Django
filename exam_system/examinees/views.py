from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from exams.models import Exam, ExamQuestionTopic
from examinees.models import Examinee, ExamineeExam
from questions.models import Question, Options
from django.db import connection, transaction
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
		exam_end_data = {'exam_id':exam_id, 'examinee_id':examinee_id}
		return render(request, 'examinees/examinee-exam-end.html', context=exam_end_data)

	question = Question.objects.get(id=exam_questions.question_id) 
	options= Options.objects.filter(question_id=question.id)
	counter = end
	exam_data = {'exam_id':exam_id, 'examinee_id':examinee_id, 
				 'question':question,'options':options,'counter':counter
				 }
	return render(request, 'examinees/demo.html', context=exam_data)
	
		#return HttpResponse(answer)

def view_report(request, exam_id, examinee_id):
	cursor = connection.cursor()

	cursor.execute('''SELECT  question, questions_options.option, questions_options.id,
					answer_id FROM questions_question, 
					examinees_examineeexam, questions_options WHERE examinee_id = examinee_id 
					AND exam_id = exam_id AND examinees_examineeexam.question_id = questions_question.id 
					AND examinees_examineeexam.question_id = questions_options.question_id 
					AND questions_options.is_answer = 1''')
	exam_report = cursor.fetchall()

	exam_data = {'exam_report':exam_report}
	return render(request, 'examinees/examinee-exam-report.html', context=exam_data)

