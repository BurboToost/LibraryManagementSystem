from django.db import models

# Create your models here.

class Member(models.Model):
    first_name= models.CharField(max_length=250)
    last_name= models.CharField(max_length=250)
    email= models.EmailField(unique=True)


    def __str__(self):
        return  f"{self.firs_name} {self.last_name}"