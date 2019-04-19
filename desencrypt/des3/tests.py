from django.test import TestCase
from .models import Quiz
# Create your tests here.

class QuizCheck(TestCase):
    """Checks if the database is runnning well and nicely and returning the questions along with their answers"""
    def returnsQuestion(self):
        o = Quiz(q_id = 1 ,q_text = "question" , option1 = "a" , option2 = "b" , option3 = "c" , option4="d" , answer = "a")
        objectQuestion = Quiz.objects.all() 
        print(len(objectQuestion))
        self.assertIs(len(objectQuestion)>0,True)
