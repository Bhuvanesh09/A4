from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

from .models import Quiz

def index(request):
    return HttpResponse("Yo boi")
# Create your views here.
def introduction(request):
    return render(request, 'Introduction.html')


def experiment(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'Experiment.html', {
        'questn': Quiz.objects.all(),
    })


def manual(request):
    return render(request, 'Manual.html')


def objective(request):
    return render(request, 'Objective.html')


def quizzes(request):
    return render(request, 'Quizzes.html')


def procedure(request):
    return render(request, 'Procedure.html')

def feedback(request):
    return render(request, 'Feedback.html')

def furtherReading(request):
    return render(request, 'FurtherReadings.html')

