import string
from django.db import models

# Create your models here.
class Tasks(models.Model):
    id=models.IntegerField
    name=models.CharField(max_length=200)
    description=models.TextField()