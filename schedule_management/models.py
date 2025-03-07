from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    CHOICES = {
        'Pro': 'Professor',
        'Opp': 'Orientador de pp'
    }
    
    user_nif = models.IntegerField()
    username = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=20)
    user_role = models.CharField(max_length=3, choices=CHOICES, default='Pro')

class OPP(User):
    pass

class Enviroment(models.Model):
    enviroment_name = models.CharField(max_length=30)

    def __str__(self):
        return self.enviroment_name

class Schedule(models.Model):
    class_time = models.CharField(max_length=20)
    accountable_teacher_name = models.CharField(max_length=100)
    classroom_enviroment = models.ForeignKey(Enviroment, on_delete=models.CASCADE)

    def __str__(self):
        return self.enviroment_name