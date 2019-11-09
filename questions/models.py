from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    soru = models.TextField()
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)
    dogru_cevap = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)




