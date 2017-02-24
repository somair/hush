from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import *

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

def movies(request):
    movies_list = Movie.objects.order_by('title')
    context = {
        'movies_list':movies_list
    }
    return render(request, 'video/movies.html', context)

def shows(request):
    #Work in Progress
    #List shows available

def episode(request):
    #Work in progress
    #List episodes belonging to selected show
