from django.urls import path
from BucketList import views

urlpatterns = [
	path('', views.home),
]