from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default="")
    name = models.TextField(default="")
    age = models.IntegerField(default=0)