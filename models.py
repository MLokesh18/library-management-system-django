from django.db import models

# Create your models here.
class User_Details(models.Model):
    Fname=models.CharField(max_length=128)
    Lname=models.CharField(max_length=128)
    User_Name=models.CharField(max_length=120)
    Password=models.IntegerField()

class Book_Details(models.Model):
    Name=models.CharField(max_length=128)
    Code=models.IntegerField()
    Author_name=models.CharField(max_length=128)
    Date=models.DateField()
    Status=models.CharField(max_length=128)
    Amount=models.IntegerField()
    Created_date=models.DateField()
    Created_by=models.IntegerField()
    Updated_date=models.DateField(null=True)
    Updated_by=models.IntegerField(null=True)

class Book_Login(models.Model):
    Name=models.CharField(max_length=128)
    Password=models.IntegerField()

class user(models.Model):
    Name=models.CharField(max_length=128)
    Code=models.IntegerField()
    Book_name=models.CharField(max_length=128)