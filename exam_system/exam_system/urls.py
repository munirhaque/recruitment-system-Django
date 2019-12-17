"""exam_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_view
from topics import views as topics_view
from questions import views as questions_view
from exams import views as exams_view
from examinees import views as examinees_view

urlpatterns = [
	# admin urls
    path('admin/', admin.site.urls),
    path('index',users_view.index),
    path('user_authentication', users_view.user_authentication, name='user_authentication'),
    path('dashboard/', users_view.dashboard, name='dashboard'),

    # topic urls
    path('topics/', topics_view.index, name='topics'),
    path('topic_questions/<int:topic_id>', topics_view.topic_questions, name='topic_questions'),
    path('topic_add', topics_view.add, name="topic_add"),
    path('topic_store', topics_view.store, name="topic_store"),
    path('topic_edit/<int:topic_id>', topics_view.edit, name='topic_edit'),
    path('topic_update/<int:topic_id>', topics_view.topic_update, name='topic_update'),
    path('topic_delete/<int:topic_id>', topics_view.destroy, name='topic_delete'),


    # Questions urls
    path('question_add/<int:topic_id>', questions_view.add,name='question_add'),
    path('question_store/<int:topic_id>', questions_view.store,name='question_store'),
    path('option_add/<int:topic_id>/<int:question_id>', questions_view.add_option,name='option_add'),
    path('option_store/<int:topic_id>/<int:question_id>', questions_view.store_option,name='option_store'),
    path('set_answer/<int:topic_id>/<int:question_id>', questions_view.set_answer,name='set_answer'),
    path('select_answer/<int:topic_id>/<int:question_id>', questions_view.select_answer,name='select_answer'),

    # Exam urls
    path('exams/', exams_view.index, name='exams'),
    path('create_exam/', exams_view.create, name='create_exam'),
    path('save_exam/', exams_view.store, name='save_exam'),
    path('select_topic/<int:exam_id>', exams_view.select_topic, name='select_topic'),
    path('select_questions/<int:exam_id>/<int:topic_id>', exams_view.select_questions, name='select_questions'),
    path('set_exam_questions/<int:exam_id>/<int:topic_id>', exams_view.set_exam_questions, name='set_exam_questions'),

    # Examinee urls
    path('examinees/', examinees_view.index, name='examinees'),
    path('examinee_login/', examinees_view.user_login, name='examinee_login'),
    path('start_exam/<int:exam_id>/<str:name>/<str:email>', examinees_view.start_exam, name='start_exam' ),
    path('submit_answer/<int:exam_id>/<int:examinee_id>/<int:question_id>/<int:counter>',examinees_view.submit_answer, name='submit_answer'),
]
