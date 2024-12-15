from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)
    examples = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Project(models.Model):
    name = models.CharField(max_length=255)
    banner_url = models.CharField(max_length=255)
    files=models.CharField(max_length=2048)
    description = models.CharField(max_length=255) 

class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message=models.CharField(max_length=2048)
