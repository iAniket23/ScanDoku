from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class user(models.Model):
    username = models.CharField('username', max_length=20, primary_key= True)
    password = models.CharField('password', max_length=20)
    email = models.EmailField('email', max_length=50)
    numberOfSudokus = models.IntegerField('numberOfSudokus', default=0)

    def __str__(self):
        return self.username

class sudoku(models.Model):
    id = models.AutoField(primary_key=True)
    digits = models.IntegerField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    
    def __int__(self):
        return self.id