from django.db import models

# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255,null=True)
    
    
    