from django.db import models

# Create your models here.
# class React(models.Model):
#     class Meta:
#         db_table = "react"
#     user = models.CharField(max_length=30)
#     team = models.CharField(max_length=50)
#     organization = models.CharField(max_length=200)
#     date_of_birth = models.DateField(null=True)




### USER MODELS ###

class User(models.Model):
    class Meta:
        db_table = 'users'
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    team = models.CharField(max_length=50, null=True)
    organization = models.CharField(max_length=50, null=True)

class Team(models.Model):
    class Meta:
        db_table = 'teams'
    team_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=50)

class Organization(models.Model):
    class Meta:
        db_table = 'organizations'
    organization_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=50)


### POSTS MODELS ###
class Post(models.Model):
    class Meta:
        db_table = 'posts'
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    content = models.CharField(max_length=500)


