from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^/?$', views.introduction, name='des3.home'),
	url(r'^introduction/?$', views.introduction, name='des3.introduction'),
	url(r'^experiment/?$', views.experiment, name='des3.experiment'),
	url(r'^manual/?$', views.manual, name='des3.manual'),
	url(r'^objective/?$', views.objective, name='des3.objective'),
	url(r'^quizzes/?$', views.quizzes, name='des3.quizzes'),
	url(r'^procedure/?$', views.procedure, name='des3.procedure'),
	url(r'^furtherReading/?$', views.furtherReading, name='des3.furtherReading'),
]