from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=300)
    length = models.IntegerField(default=0)
    frequency = models.IntegerField(default=0)

    def __str__(self):
        return self.word
