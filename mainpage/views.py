from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def MainIndexView(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect("home/")
        else:
            messages.info(request, 'Invalid Username OR Password')
            return redirect('/')

    else:
        return render(request, 'mainpage/mainIndex.html')