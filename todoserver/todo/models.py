from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)