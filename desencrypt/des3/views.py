from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Yo boi")
# Create your views here.
