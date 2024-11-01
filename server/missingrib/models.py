from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.TextField(default="")
    age = models.IntegerField(default=0)