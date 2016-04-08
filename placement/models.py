from django.db import models

# Create your models here.
class Candidate(models.Model):
    cid =  models.CharField(primary_key=True, max_length = 10)
    username = models.CharField(max_length = 10, unique=True)
    password = models.CharField(max_length = 30)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    dob = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 6)
    mobile = models.IntegerField(unique=True)
    grad = models.CharField(max_length = 2)
    course = models.CharField(max_length = 30)
    college = models.CharField(max_length = 100)
    city = models.CharField(max_length = 25)
    zip = models.IntegerField()
    mark = models.FloatField(default="0")
    rank = models.IntegerField(default="0")

    def __unicode__(self):
        return self.username

class Recruiter(models.Model):
    rid = models.CharField(primary_key=True, max_length = 10)
    username = models.CharField(unique=True, max_length = 10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 30)
    name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.username

class Interview(models.Model):
    cid = models.CharField(max_length = 10)
    rid = models.CharField(max_length = 10)
    mark = models.IntegerField()
    
    def __unicode__(self):
        return self.cid