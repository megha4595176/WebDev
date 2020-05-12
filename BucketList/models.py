from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListItem(models.Model):
	team = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	content = models.CharField(max_length=500)
	deadline = models.DateField()
	member = models.CharField(max_length=100)
   
class ListNotif(models.Model):
	task = models.CharField(max_length=500)
	member2 = models.CharField(max_length=100)
	status = models.CharField(max_length=100)   

class Profile(models.Model):
    memberid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    mem = models.TextField(max_length=30, blank=True, null=True)
    







