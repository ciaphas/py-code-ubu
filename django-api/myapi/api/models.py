from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# Create your models here.