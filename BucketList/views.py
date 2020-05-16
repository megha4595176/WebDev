from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ListItem,Profile,Leader
from .forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import operator
from django.contrib import messages

'''from datetime import timedelta
import datetime
import pytz

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

service_account_email = 'bucketlistadmin@bucketlist-2001.iam.gserviceaccount.com'

CLIENT_SECRET_FILE = 'bucketlist-2001-58a3dfd48f62.json'

SCOPES = 'https://www.googleapis.com/auth/calendar'
scopes = [SCOPES]

def build_service():
	credentials = ServiceAccountCredentials.from_json_keyfile_name(filename='bucketlist-2001-58a3dfd48f62.json',scopes=SCOPES)
	http = credentials.authorize(httplib2.Http())
	service = build('calendar', 'v3', http=http)
	return service'''

'''def create_event():
   service = build_service()
    start_datetime = datetime.datetime.now(tz=pytz.utc)
	event = service.events().insert(calendarId='shreyayadav987@gmail.com', body={'summary': 'Foo','description': 'Bar','start': {'dateTime': start_datetime.isoformat()},'end': {'dateTime': (start_datetime + timedelta(minutes=15)).isoformat()} ,}).execute()
	print(event)'''


# Create your views here.
def home(request, leadsignedin={}):
	context={
	'leadsignedin':False
	}
	if request.user.is_authenticated:
		all_member= Profile.objects.filter(memberid__id=request.user.id)
		all_items = ListItem.objects.filter(team__id=request.user.id)
		allitems = all_items.filter(status="Incomplete")
		TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
		context.update(leadsignedin)
		return render(request,'BucketList/home.html',{'all':allitems,'all_members':all_member,'teamleader':TeamLeader,'leadsignedin':leadsignedin,'notifs':all_items})
	else:
		return render(request,'BucketList/home.html',{})

def add(request):
	new_item= ListItem(content=request.POST['content'],member=request.POST['member'],deadline=request.POST['deadline'],team=request.user)
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	flag=0;
	for member in all_member:
		if(new_item.member == member.mem):
			new_item.save()
			return HttpResponseRedirect('/')
			flag=1;
	if(flag==0):
		messages.info(request,"Work could not be added as it was assigned to a non-existent member")
		return HttpResponseRedirect('/')

def addMember(request):
	new_mem= Profile(mem=request.POST['memname'],memberid=request.user)
	new_mem.save()
	return HttpResponseRedirect('/')

def addLeader(request):
	leader=Leader(Group_leader=request.POST['Leader'],leaderid=request.user,leader_pin="abcd")
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	flag=0;
	for member in all_member:
		if(leader.Group_leader == member.mem):
			leader.save()
			messages.info(request,"Your pin is abcd.")
			return HttpResponseRedirect('/')
			flag=1;
	if(flag==0):
		messages.info(request,"Leader could not be added as it was assigned to a non-existent member")
		return HttpResponseRedirect('/')

def delete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	item_d.delete()
	return HttpResponseRedirect('/')

def complete(request,item_id):
	item_d= ListItem.objects.get(id=item_id)
	item_d.status="Completed :)"
	item_d.save()
	return HttpResponseRedirect('/')

def change(request,item_id):
	flag=0;
	members=Profile.objects.filter(memberid__id=request.user.id)
	new_mem=request.POST['memchange']
	for member in members:
		if(new_mem == member.mem):
			item_d= ListItem.objects.filter(id=item_id).update(member=request.POST['memchange'])
			flag=1;
	if(flag==0):
		messages.info(request,"Member is not a part of the team!")
	return HttpResponseRedirect('/')

def sortbydead(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	stuff = ListItem.objects.filter(team__id=request.user.id) 
	allitems = stuff.filter(status="Incomplete")
	all_items = allitems.order_by('deadline')
	return render(request,'BucketList/home.html',{'all':all_items,'all_members':all_member,'notifs':stuff,'teamleader':TeamLeader})

def sortbymem(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	stuff = ListItem.objects.filter(team__id=request.user.id)
	allitems = stuff.filter(status="Incomplete")
	all_items = allitems.order_by('member')
	return render(request,'BucketList/home.html',{'all':all_items,'all_members':all_member,'notifs':stuff,'teamleader':TeamLeader})

def unsort(request):
	all_member= Profile.objects.filter(memberid__id=request.user.id)
	TeamLeader= Leader.objects.filter(leaderid__id=request.user.id)
	all_items=ListItem.objects.filter(team__id=request.user.id)
	allitems = all_items.filter(status="Incomplete")
	return render(request,'BucketList/home.html',{'all':allitems,'all_members':all_member,'notifs':all_items,'teamleader':TeamLeader})

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
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
		else:
			print(user_form.errors)
	else:
		user_form = Userform()
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
			messages.info(request,"Wrong username/password!")
			return render(request,'BucketList/login.html', {})
	else:
		return render(request,'BucketList/login.html', {})

def signasleader(request):
	leadersignin=False
	leaderpin=request.POST.get('leaderpin')
	leader= Leader.objects.get(leaderid__id=request.user.id)
	if(leaderpin == leader.leader_pin):
		leadersignin=True
		context={'leadsignedin':leadersignin}
		response=home(request, context)
		return response
	else:
		messages.info(request,"Wrong pin!")
		return HttpResponseRedirect('/')