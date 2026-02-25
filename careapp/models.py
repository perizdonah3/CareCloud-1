from django.db import models

# Create your models here.

class Patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname =models.CharField(max_length=50)
    dob = models.DateField()
    age =models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered =models.DateTimeField()
    medicalhistory =models.TextField()
    def __str__(self):
        return self.firstname + self.lastname

#Create a model for storing doctor information
#first_name,last_name,Specialization
#Phone_number,email,years_of_experience


class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    yearsofexperience = models.PositiveIntegerField()

    def __str__(self):
        return self.firstname


class MyAppointments(models.Model):
        name = models.CharField(max_length=200)
        email =models.EmailField()
        phonenumber =models.CharField(max_length=20)
        datetime =models.DateTimeField()
        department =models.CharField(max_length=10)
        doctor =models.CharField(max_length=100)
        message =models.TextField()

        def __str__(self):
            return self.name