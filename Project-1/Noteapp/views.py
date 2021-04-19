from django.shortcuts import render,redirect
from Noteapp.forms import UsForm,ImForm,UtupForm,ChpasForm
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from Noteapp.models import ImProfile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

def home(request):
	# t = User.objects.all()
	# print(t)
	t = User.objects.all()
	r = {}
	for l in t:
		g = ImProfile.objects.get(uid_id=l.id)
		r[l.id]=g.impf,l.username,l.email
	m = r.values()
	return render(request,'stc/home.html',{'m':m})

def about(request):
	return render(request,'stc/about.html')

def contact(request):
	return render(request,'stc/contact.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST or None)
		if p.is_valid():
			p.save()
			# User.objects.create(**p.cleaned_data)
			return redirect('/lg')
		else:
			for k in p.errors:
				messages.warning(request,p.errors[k])
			# messages.warning(request,p['password1'].errors)
			# messages.warning(request,p['password2'].errors)
	p=UsForm()
	return render(request,'stc/register.html',{'u':p})

@login_required
def dashboard(request):
	m = User.objects.all()
	paginator = Paginator(m,3)
	page_number = request.GET.get('page')
	po = Paginator.get_page(paginator,page_number)
	return render(request,'stc/dashboard.html',{'da':m,'pg':po})

@login_required
def profile(req):
	d=ImForm()
	return render(req,'stc/profile.html',{'d':d})

@login_required
def updpf(request):
	if request.method == "POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'stc/updateprofile.html',{'us':u,"imp":i})

@login_required
def chpswd(request):
	if request.method == "POST":
		o = ChpasForm(user=request.user,data=request.POST)
		if o.is_valid():
			o.save()
			return redirect('/pro')
	o = ChpasForm(user=request.user)
	return render(request,'stc/changepassword.html',{'c':o})