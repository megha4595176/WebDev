from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ListItem(models.Model):
	team = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	content = models.CharField(max_length=500,blank=True,null=True,default=None)
	deadline = models.DateField()
	member = models.CharField(max_length=100,blank=True,null=True)
	status=models.TextField(max_length=20,default="Incomplete")


class Profile(models.Model):
    memberid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    mem = models.TextField(max_length=30, blank=True, null=True)
    
class Leader(models.Model):
	leaderid=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
	Group_leader=models.TextField(max_length=30, blank=True, null=True)
	leader_pin=models.TextField(max_length=4,blank=True, null=True)

