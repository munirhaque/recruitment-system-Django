from django.shortcuts import render, redirect
from django.http import HttpResponse
from topics.models import Topic
from questions.models import Question
from questions.models import Options
from django.contrib import messages
# Create your views here.

def add(request, topic_id):
	topic = {'topic_id':topic_id}
	return render(request, 'questions/admin-add-question.html', context=topic)

def store(request, topic_id):
	if request.method == 'POST':
		question = request.POST['question']
		Question.objects.create(question = question, topic_id = topic_id)
		messages.success(request, '<div class="alert alert-success">Question Added Successfully!</div>')
		return redirect('topic_questions', topic_id=topic_id)


def add_option(request, topic_id, question_id):
	question = Question.objects.get(id=question_id)
	options = Options.objects.filter(question_id=question_id)
	question_data = {'question':question, 'topic_id':topic_id, 'options':options}
	return render(request, 'questions/admin-add-option.html', context=question_data)


def store_option(request, topic_id, question_id):
	if request.method == 'POST':
	   option=request.POST['option']
	   Options.objects.create(option = option, question_id = question_id)
	   return redirect('option_add', topic_id, question_id)

def set_answer(request, topic_id, question_id):
	question = Question.objects.get(id=question_id)
	options = Options.objects.filter(question_id=question_id)
	question_data = {'question':question, 'options':options, 'topic_id':topic_id}
	return render(request, 'questions/admin-set-answer.html',context=question_data)

def select_answer(request, topic_id, question_id):
	if request.method == 'POST':
		answer = request.POST['answer']
		option = Options.objects.filter(question_id=question_id)
		option.update(is_answer = None)
		option = Options.objects.filter(id=answer).update(is_answer=1)
		return redirect('topic_questions', topic_id=topic_id)
		#return HttpResponse(str(answer))


def edit(request, topic_id, question_id):
	question = Question.objects.get(id=question_id)
	question_data = {'question':question, 'topic_id': topic_id}
	return render(request,'questions/admin-edit-question.html', context=question_data)


def update_question(request, topic_id, question_id):
	if request.method == 'POST':
		question = request.POST['question']
		Question.objects.filter(id=question_id).update(question=question)
		question_data = {'topic_id':topic_id}
		messages.success(request, '<div class="alert alert-success">Question Edited Successfully!</div>')
		return redirect('topic_questions', topic_id=topic_id)

def destroy(request, topic_id, question_id):
	Question.objects.filter(id=question_id).delete()
	messages.success(request, '<div class="alert alert-success">Question Deleted Successfully!</div>')
	return redirect('topic_questions', topic_id=topic_id)