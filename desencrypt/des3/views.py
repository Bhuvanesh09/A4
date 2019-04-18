from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

from .models import Quiz

def index(request):
    return HttpResponse("Hello!  Surver up and running , kindly open /introduction to enter the lab.")
# Create your views here.


def introduction(request):
    return render(request, 'Introduction.html')

def experiment(request):
    return render(request, 'Experiment.html')


def manual(request):
    return render(request, 'Manual.html')


def objective(request):
    return render(request, 'Objective.html')


def quizzes(request):
    assert isinstance(request, HttpRequest)
    context = {
        'questn': Quiz.objects.all(),
    }
    return render(request, 'Quizzes.html' , context)


def procedure(request):
    return render(request, 'Procedure.html')

def feedback(request):
    return render(request, 'Feedback.html')

def furtherReading(request):
    return render(request, 'FurtherReadings.html')

def theory(request):
    return render(request, 'Theory.html')

