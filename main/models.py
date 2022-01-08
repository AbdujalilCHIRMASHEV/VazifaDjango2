from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Yonalish(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Student(models.Model):
    yonalish = models.ForeignKey(Yonalish, on_delete=CASCADE)
    ism = models.CharField(max_length=255)
    yoshi = models.IntegerField()
    rasmi = models.ImageField(upload_to="Rasmlar/")

    def __str__(self):
        return self.ism