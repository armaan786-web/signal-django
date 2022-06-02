from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s)" % (self.name,self.hod)
    

class Notice(models.Model):
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(to=Branch,on_delete=models.CASCADE,null=True,blank=True)


class profile(models.Model):
    user = models.OneToOneField(to=User,on_delete=models.CASCADE)
    branch = models.ForeignKey(to=Branch,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.user.username
    