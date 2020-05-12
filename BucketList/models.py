from django.db import models

# Create your models here.
class ListItem(models.Model):
	content = models.CharField(max_length=500)
	deadline = models.DateField()
	member = models.CharField(max_length=100)
   
class ListNotif(models.Model):
	task = models.CharField(max_length=500)
	member2 = models.CharField(max_length=100)
	status = models.CharField(max_length=100)   