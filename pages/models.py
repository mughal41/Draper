from django.db import models
from django import forms
from django.core import validators
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class BloodGroup(models.Model):
    name = models.CharField(max_length=5)
 
    def __str__(self):
        return self.name
class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        return self.name
 
class Donor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    ready_to_donate = models.BooleanField(default=True)
 
    def __str__(self):
        return str(self.blood_group)

class Donorinfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postalcode = models.IntegerField()
    country = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=10)
    phonenumber = models.IntegerField()
    email = models.EmailField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = models.Manager

    def get_absolute_url(self):
        return reverse('Donor',kwargs={'pk': self.pk})

class Postform(forms.ModelForm):
    class Meta:
        model = Donorinfo
        fields = ['firstname', 'lastname','address','city','state','postalcode','country','bloodgroup','phonenumber','email']

