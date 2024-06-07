from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True)
    dateOfBirth = models.DateField()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

