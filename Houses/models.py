from django.db import models

# Create your models here.

class Customer(models.Model):
    First_Name=models.CharField(max_length=15,unique=True)
    Last_Name=models.CharField(max_length=15,unique=True)
    Email=models.EmailField(max_length=25,unique=True)
    Contact=models.CharField(max_length=10,unique=True)
    username=models.CharField(max_length=15,primary_key=True)
    password=models.CharField(max_length=180)
    CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]
    Gender=models.CharField(max_length=6,choices=CHOICES)
    City=models.CharField(max_length=10,choices=[('Mumbai','Mumbai'),('Chennai','Chennai'),('Delhi','Delhi'),('Kolkata','Kolkata'),('Banglore','Banglore'),('Indore','Indore'),('Hyderabad',"Hyderabad"),('Ahmedbad','Ahmedbad'),('Amritsar',"Amritsar"),('Jaipur','Jaipur')])
    Address_Line_1=models.CharField(max_length=50)
    Address_Line_2=models.CharField(max_length=50)
    PinCode=models.CharField(max_length=6)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username
