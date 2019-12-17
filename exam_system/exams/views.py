from django.shortcuts import render, redirect
from django.http import HttpResponse
from exams.models import Exam, ExamQuestionTopic
from topics.models import Topic
from questions.models import Question
from datetime import date

# Create your views here.
def index(request):
	exams = Exam.objects.filter(start_date__gt=date.today())
	exam_data = {'exams':exams}
	return render(request, 'exams/admin-exams.html', context=exam_data)

def create(request):
	return render(request, 'exams/admin-create-exams.html')

def store(request):
	if request.method == 'POST':
		exam_name = request.POST['exam_name']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		number_of_questions = request.POST['number_of_questions']
		time_duration = request.POST['time_duration']
		Exam.objects.create(name=exam_name, start_date=start_date,end_date=end_date,
				number_of_question = number_of_questions, time_duration= time_duration)
		return redirect("exams")

def select_topic(request, exam_id):
	topics = Topic.objects.all()
	exam = Exam.objects.get(id=exam_id)
	#questions_set = exam.question.all().count()
	#questions_set = Exam.Question.get(exam_id=exam_id).count()
	topic_data = {'topics':topics, 'exam':exam }
	return render(request, 'exams/admin-select-topic.html', context=topic_data)


def select_questions(request, exam_id, topic_id):
	topic = Topic.objects.get(id=topic_id)
	total_questions = Question.objects.filter(topic_id=topic_id).count()
	no_of_question_selected = ExamQuestionTopic.objects.filter(topic_id=topic_id, exam_id=exam_id).count()
	exam = Exam.objects.get(id=exam_id)
	remain_question_selection = exam.number_of_question - no_of_question_selected
	data = {'topic':topic, 'total_questions':total_questions, 'exam':exam, 
			'no_of_question_selected':no_of_question_selected,
			'remain_question_selection':remain_question_selection }
	return render(request, 'exams/admin-set-questions.html', context=data)


def set_exam_questions(request, exam_id, topic_id):
	if request.method == 'POST':
	   number_of_questions = int(request.POST['number_of_questions'])
	   select_questions = Question.objects.filter(topic_id=topic_id).order_by('?')[:number_of_questions].only('id')
	   
	   #questions = {'selected_questions':select_questions}
	   #select_questions = Question.objects.filter(topic_id=topic_id).order_by('?')[:number_of_questions].only('id')
	   #question_data = {'selected_questions':select_questions}
	   #for question in select_questions:
	   #exam = Exam.objects.get(id=exam_id)
	   #exam.topic.objects.create(exam_id=exam_id, topic_id=topic_id)
	   #questions = None
	   for question in select_questions:
	   		ExamQuestionTopic.objects.create(exam_id = exam_id, question_id=question.id, topic_id=topic_id)
	   	
	   return redirect('select_topic', exam_id) 
	   
	   # for question in select_questions:
	   # 		exam.question.create(exam_id=exam_id, question_id=question.id)
	   		#return HttpResponse(question.id)
	   
	   #return HttpResponse(select_questions.id)
	   #MyModel.objects.order_by('?')
	   #return HttpResponse(str(number_of_questions) + "<br/>" + str(exam_id) + "<br/>" + str(topic_id))

