from tkinter import CASCADE
from typing import Text
import django
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
User = django.contrib.auth.get_user_model()

class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default=datetime.today)
    Published_date = models.DateTimeField(default=datetime.today)

def __str__(User):
    return User.title
