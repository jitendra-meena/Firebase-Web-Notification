from dis import code_info
from operator import mod
from django.db import models




class RegisterInfo(models.Model):
    name = models.CharField(max_length=20,blank=True)
    dob = models.DateField(max_length=8,default=0)
    gender = models.CharField(max_length=30,blank=True)
    county = models.CharField(max_length=20,blank=True)
    code_info = models.CharField(max_length=70)
    notification = models.BooleanField(default=True)


    def __str__(self):
        return self.name

