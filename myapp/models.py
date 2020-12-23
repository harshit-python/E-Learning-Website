from django.db import models

class Tutorial(models.Model):
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, default="")

class Quiz(models.Model):
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, default="")
    creator = models.CharField(max_length=1000, default="")

class MockTest(models.Model):
    desc = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, default="")
    creator = models.CharField(max_length=1000, default="")
    
    