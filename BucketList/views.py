from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ListItem
import operator

# Create your views here.
def home(request):
	all_items = ListItem.objects.all()
	return render(request,'BucketList/home.html',{'all':all_items})

def add(request):
	new_item= ListItem(content=request.POST['content'],member=request.POST['member'],deadline=request.POST['deadline'])
	new_item.save()
	return HttpResponseRedirect('/')

def delete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	item_d.delete()
	return HttpResponseRedirect('/')

def sortbydead(request):
	all_items = ListItem.objects.order_by('deadline')
	return render(request,'BucketList/home.html',{'all':all_items})

def sortbymem(request):
	all_items = ListItem.objects.order_by('member')
	return render(request,'BucketList/home.html',{'all':all_items})

def unsort(request):
	all_items=ListItem.objects.all()
	return render(request,'BucketList/home.html',{'all':all_items})



