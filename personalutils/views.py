import re
from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.contrib import auth, messages

def home(request:HttpRequest):
    return render(request,"comun/home.html")

def login(request:HttpRequest):
    if request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user= auth.authenticate(request=request, username=username,password=password)
            
            if user:
                auth.login(request=request,user=user)
                messages.success(request=request, message="You have login sucsessfully ")
                return redirect("/")
            messages.error(request=request, message="Fail to login user user not found")

        except Exception as e:
            messages.error(request=request, message="Fail to login user")
    return render(request,"comun/login.html")