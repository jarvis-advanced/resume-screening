from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.http import HttpResponse, Http404

# Landing page
def index(request):

	return render(request, 'index.html',)

@login_required
def home(request):
    return render(request,"home.html")
