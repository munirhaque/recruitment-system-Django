from django.shortcuts import render, redirect
from django.http import HttpResponse
from topics.models import Topic
from questions.models import Question, Options 

# Create your views here.
def index(request):
	topics = Topic.objects.all()
	topic_data = {'topics':topics}
	return render(request, 'topics/admin-topics.html', context=topic_data)


def topic_questions(request, topic_id):
	questions = Question.objects.filter(topic_id=topic_id)
	topic = Topic.objects.get(id=topic_id)
	questions_data = {'questions':questions, 'topic':topic}
	return render(request, 'topics/admin-topic-questions.html', context=questions_data)


def add(request):
	return render(request, 'topics/admin-add-topic.html')

def store(request):
	if request.method == 'POST':
	  topic_name = request.POST['topic_name']
	  Topic.objects.create(topic_name=topic_name)
	  success_msg = {'msg':'success'}
	  return redirect('topics/', context=success_msg)


def edit(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	topic_data = {'topic':topic}
	return render(request, 'topics/admin-edit-topic.html',context=topic_data)



def topic_update(request, topic_id):
	if request.method == 'POST':
		topic_name = request.POST['topic_name']
		Topic.objects.filter(pk=topic_id).update(topic_name=topic_name)
		return HttpResponse(index(request))



def destroy(request, topic_id):
	Topic.objects.filter(id=topic_id).delete()
	success_msg = {'msg':'success'}
	return HttpResponse(index(request))


# Create your views here.
