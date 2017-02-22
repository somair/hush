from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

def logout(request):
	auth.logout(request)
	return redirect('/login/')

@login_required(login_url='/login/')
def video(request):
    return render(request, 'video.html')
