from django.shortcuts import render,redirect
from . forms import Usrg,UpdaPfl,Im,CreatNot,UpNts
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Updf,CrNt
from django.contrib.auth.models import User
from django.http import HttpResponse
import secrets

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		p = Usrg(request.POST)
		if p.is_valid():
			p.save()
			messages.success(request,"You have successfully registered")
			return redirect('/login')
	p = Usrg()
	return render(request,'html/register.html',{'k':p})

@login_required
def dashboard(request):
	z = CrNt.objects.filter(crt_id=request.user.id).count()
	d = "{:02}".format(z)
	k = CrNt.objects.all()
	zy = []
	for h in k:
		zy.append(h.id)
		pass
	ss = zy[-1]-int(d)
	ss = "{:02}".format(ss)
	return render(request,'html/dashboard.html',{'cr':d,'dl':ss})

@login_required
def prfle(request):
	return render(request,'html/profile.html')

def updfple(request):
	if request.method == "POST":
		m = UpdaPfl(request.POST,instance=request.user)
		n = Im(request.POST,request.FILES,instance=request.user.updf)
		if m.is_valid() and n.is_valid():
			m.save()
			n.save()
			messages.success(request,"Profile updated Successfully")
			return redirect('/pfle')
	m = UpdaPfl(instance=request.user)
	n = Im(instance=request.user.updf)
	return render(request,'html/updateprofile.html',{'p':m,'r':n})

@login_required
def notesview(request):
	l = CrNt.objects.filter(crt_id=request.user.id)
	r = CrNt.objects.all()
	z = []
	for i in r:
		if i.created_by == request.user.username:
			continue
		else:
			z.append(i)
	return render(request,'html/notesview.html',{'mn':l,'al':z})

@login_required
def crnotes(request):
	if request.method == "POST":
		k = CreatNot(request.POST,request.FILES)
		if k.is_valid():
			m = k.save(commit=False)
			m.created_by=request.user.username
			m.gnkey = secrets.token_hex(10)
			m.crt_id = request.user.id
			m.save()
			messages.success(request,"{} Notes Added Successfully".format(m.title))
			return redirect('/vwnt') 
	k = CreatNot()
	return render(request,'html/crtnt.html',{'p':k})

# a7651867980596945e92

@login_required
def updatent(request,pk):
	c = CrNt.objects.get(id=pk)
	if request.method == "POST":
		g = UpNts(request.POST,request.FILES,instance=c)
		if g.is_valid():
			g.save()
			messages.success(request,"{} Notes Updated Successfully".format(c.title))
			return redirect("/vwnt")
	g = UpNts(instance=c)
	return render(request,'html/upnts.html',{'y':g})

@login_required
def deletent(request,pj):
	s = CrNt.objects.get(id=pj)
	if request.method == "POST":
			s.delete()
			messages.warning(request,"{} Notes Deleted Successfully".format(s.title))
			return redirect('/vwnt')
	return render(request,'html/deltnt.html',{'t':s})

