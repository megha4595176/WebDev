from __future__ import unicode_literals


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

class Event(models.Model):
	day = models.DateField(u'Day of the event', help_text=u'Day of the event')
	end_time = models.TimeField(u'deadline', help_text=u'deadline')
	notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes')

	class Meta:
		verbose_name = u'Scheduling'
		verbose_name_plural = u'Scheduling'

	def get_absolute_url(self):
		url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
		return u'<a href="%s">%s</a>' % (url, str(self.start_time))
