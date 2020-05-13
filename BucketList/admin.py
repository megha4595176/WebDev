from django.contrib import admin
from BucketList.models import User,ListItem,Profile,Leader
# Register your models here.
admin.site.register(Profile)
admin.site.register(ListItem)
admin.site.register(Leader)