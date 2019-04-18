from django.db import models

# Create your models here.

class Quiz(models.Model):
    q_id = models.IntegerField()
    q_text = models.CharField(max_length = 400)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.q_text + ' [' + str(self.option1) + ']' + ' [' + str(self.option2) + ']' + ' [' + str(self.option3) + ']' + ' [' + str(self.option4) + ']'
