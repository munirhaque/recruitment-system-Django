from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext


def index(request):
  	 return render(request, 'login.html')


def user_authentication(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		user_data = {'user':user}
		if user is not None:
		 	login(request, user)
		 	return redirect('dashboard/', context=user_data)


def dashboard(request):
	return render(request, 'index.html')