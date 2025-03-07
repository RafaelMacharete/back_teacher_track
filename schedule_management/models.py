from django.db import models

# Create your models here.
class User(models.Model):
    CHOICES = {
        'Pro': 'Professor',
        'Opp': 'Orientador de pp'
    }
    
    user_nif = models.IntegerField()
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=20)
    user_role = models.CharField(max_length=3, choices=CHOICES, default='Pro')

    def __str__(self):
        return self.user_name

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Enviroment(models.Model):
    enviroment_name = models.CharField(max_length=30)

    def __str__(self):
        return self.enviroment_name

class Schedule(models.Model):
    class_time = models.CharField(max_length=20)
    accountable_teacher_name = models.CharField(max_length=100)
    classroom_enviroment = models.ForeignKey(Enviroment, on_delete=models.CASCADE)

    def __str__(self):
        return self.accountable_teacher_name