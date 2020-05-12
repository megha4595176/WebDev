from django.contrib import admin
from BucketList.models import User,ListItem,Profile
# Register your models here.
admin.site.register(Profile)
admin.site.register(ListItem)