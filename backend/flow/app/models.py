from django.db import models

# Create your models here.
class React(models.Model):
    user = models.CharField(max_length=30)
    team = models.CharField(max_length=50)
    organization = models.CharField(max_length=200)