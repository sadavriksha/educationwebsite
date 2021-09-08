from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=20,default="")
    phone = models.CharField(max_length=13,default="")
    address = models.CharField(max_length=50,default="")
    course = models.CharField(max_length=100,default="")
    school = models.CharField(max_length=50,default="")
    date = models.DateField(max_length=20,default="")
