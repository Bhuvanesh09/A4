from django.db import models

# Create your models here.

class Quiz(models.Model):
    q_text = models.CharField(max_length = 400)
    option1 = models.CharField()
    option2 = models.CharField()
    option3 = models.CharField()
    option4 = models.CharField()
    answer = models.CharField()
