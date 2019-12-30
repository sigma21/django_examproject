from django.db import models
from django.contrib.auth.models import User
from accounts.models import Account


class Question(models.Model):
    user = models.ManyToManyField(Account, through='Account_Question')
    text = models.TextField()
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    answer = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.id)


class Account_Question(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=20)

    
    def __str__(self):
        return str(self.id)