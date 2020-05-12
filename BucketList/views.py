from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ListItem,Profile
from .forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import operator

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		all_member= Profile.objects.filter(memberid__id=request.user.id)
		all_items = ListItem.objects.filter(team__id=request.user.id)
		return render(request,'BucketList/home.html',{'all':all_items,'all_members':all_member})
	else:
		return render(request,'BucketList/home.html',{})

def add(request):
	new_item= ListItem(content=request.POST['content'],member=request.POST['member'],deadline=request.POST['deadline'],team=request.user)
	new_item.save()
	return HttpResponseRedirect('/')

def addMember(request):
	new_mem= Profile(mem=request.POST['memname'],memberid=request.user)
	new_mem.save()
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

def addnotif(request):
	new_item= ListNotif(task=request.POST['task'],member2=request.POST['member2'],status=request.POST['status'])
	new_item.save()
	return HttpResponseRedirect('/')

     
@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = Userform(data=request.POST)
		#profile_form = Userform(data=request.POST)
		if user_form.is_valid(): #and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			#profile=profile_form.save(commit=False)
			#profile.save()
			registered=True
		else:
			print(user_form.errors)
	else:
		user_form = Userform()
		#profile_form = ProfileForm()
	return render(request,'BucketList/registrations.html',{'user_form':user_form,'registered':registered})

def user_login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user:
			login(request,user)
			return HttpResponseRedirect(reverse('home'))
		else:
			return HttpResponse("invalid login details")
	else:
		return render(request,'BucketList/login.html', {})

