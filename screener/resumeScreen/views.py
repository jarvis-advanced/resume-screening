from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.http import HttpResponse, Http404

from .models import  UploadResume
from resumeScreen.forms import UserSignupForm,UploadDes,UploadRes

# Landing page
def index(request):

	showAll= UploadResume.objects.filter(name=request.user)

	form1 = UploadDes()
	form2 = UploadRes()
	if request.method == "POST":
		
		form1 = UploadDes(request.POST, request.FILES,prefix="form1")
		form2 = UploadRes(request.POST, request.FILES,prefix="form2")
		
		if form1.is_valid() and form2.is_valid():
			des = form1.save(commit=False)
			res = form2.save(commit=False)
			des.name = request.user
			res.name = request.user
			des.save()
			res.save()
			return redirect('index')

		else:
			form1 = UploadDes()
			form2 = uploadRes()

	context_dict = {
		'form1' : form1,
		'form2':form2,}
	return render(request,"index.html",context_dict)

def user_registration(request):
	if request.method == 'POST':
		form=UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
		
		messages.success(request,"Account Created Successfully")
		print(request.FILES.getlist("file"))
		return redirect('index')
		
	else:
		form = UserSignupForm()
	
	return render(request,'registration/signup.html',{'form':form})

@login_required
def uploadDes(request):
	
	showAll= UploadImage.objects.filter(name=request.user)

	form = UploadDes()
	if request.method == "POST":
		
		form = UploadDes(request.POST, request.FILES)
		if form.is_valid():
			des = form.save(commit=False)
			des.name = request.user
			des.save()
			return redirect('upload')

		else:
			form = UploadDes()

	context_dict = {
		'form' : form,
		'showAll':showAll,}
	return render(request,"index.html",context_dict)
