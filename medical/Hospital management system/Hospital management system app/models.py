from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    message = models.TextField(max_length=122)
    date = models.DateField()
    
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    doctor = models.CharField(max_length=12)
    date = models.DateField()
    department = models.CharField(max_length=12)
    message = models.TextField(max_length=122)
    
    
    def __str__(self):
        return self.name



class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)
    # Add more fields as needed

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    # Add more fields as needed

    def __str__(self):
        return self.name
    
class PatientInquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    inquiry = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return self.full_name
    