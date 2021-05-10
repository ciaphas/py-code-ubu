from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    weakness = models.CharField(max_length=250)
    backstory = models.TextField(max_length=2000)


    def __str__(self):
        return self.name

# Create your models here.
