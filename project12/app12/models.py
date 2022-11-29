from django.db import models

class studentMode(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.IntegerField(unique=True)
    gender = models.CharField(max_length=15)
    username = models.CharField(unique=True, max_length=30)

class loginMode(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class adminMode(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=20)