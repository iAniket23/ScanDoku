from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class user(models.Model):
    userID = models.AutoField('userID', primary_key=True)
    username = models.CharField('username', max_length=20)
    password = models.CharField('password', max_length=20)

    def __int__(self):
        return self.userID

class sudoku(models.Model):
    sudokuID = models.AutoField("sudokuID", primary_key=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    row1 = models.IntegerField("row1", default=0)
    row2 = models.IntegerField("row2", default=0)
    row3 = models.IntegerField("row3", default=0)
    row4 = models.IntegerField("row4", default=0)
    row5 = models.IntegerField("row5", default=0)
    row6 = models.IntegerField("row6", default=0)
    row7 = models.IntegerField("row7", default=0)
    row8 = models.IntegerField("row8", default=0)
    row9 = models.IntegerField("row9", default=0)
    
    
    def __int__(self):
        return self.sudokuID

class image(models.Model):
    imageID = models.AutoField("imageID", primary_key=True)
    imageValue = models.ImageField("imageValue", upload_to="sudoku_images")

    def __int__(self):
        return self.imageID