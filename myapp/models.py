import email
from statistics import mode
from django.db import models

# Create your models here.
class signup_master(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.BigIntegerField()
   


class notes(models.Model):
    topic=models.CharField(max_length=100)
    selectop=models.CharField(max_length=50)
    des=models.TextField()
    myfile=models.FileField(upload_to='NotesUpload')

class contactdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    message=models.TextField()