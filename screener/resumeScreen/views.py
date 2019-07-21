from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.http import HttpResponse, Http404

from resumeScreen.forms import UserSignupForm

# Landing page
def index(request):

	return render(request, 'index.html',)

@login_required
def home(request):
    return render(request,"home.html")

def user_registration(request):
	if request.method == 'POST':
		form=UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
		
		messages.success(request,"Account Created Successfully")
		print(request.FILES.getlist("file"))
		return redirect('home')
		
	else:
		form = UserSignupForm()
	
	return render(request,'registration/signup.html',{'form':form})

@login_required
def uploadDes(request):
    