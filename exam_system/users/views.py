from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages

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
		else:
			messages.success(request, 'Invalid username or password')
			return redirect('index')


def dashboard(request):
	return render(request, 'index.html')

def user_logout(request):
	logout(request)
	messages.success(request, '<div class="text-danger text-center">Your are Logged out</div>')
	return redirect('index')