from django.db import models

# Create your models here.
class ListItem(models.Model):
	content = models.CharField(max_length=500)
	deadline = models.DateField()
	member = models.CharField(max_length=100)
