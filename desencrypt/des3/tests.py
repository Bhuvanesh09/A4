from django.test import TestCase
from .models import Quiz
# Create your tests here.

class QuizCheck(TestCase):
    """Checks if the database is runnning well and nicely and returning the questions along with their answers"""
    def returnsQuestion(self):
        objectQuestion = Quiz.objects.all() 
        print(len(objectQuestion))
        self.assertIs(len(objectQuestion)>0,True)
