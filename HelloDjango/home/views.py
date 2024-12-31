from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from . import views


# @login_required
def index(request):
    user = request.user
    print(user)
    if user.is_authenticated:
        return render(request, "home/index.html")
    else:
        return redirect("/login/")

def user_login(request):
    method = request.method
    if method == "GET":
        return render(request, "home/login.html")
    elif method == "POST":
        data = request.POST
        print(data)
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            ret = login(request, user)
            print(ret)
        return redirect("/")
        
    return HttpResponse(status=201)

def user_logout(request):
    logout(request)
    user = request.user
    print("after logoutout , user is ", user)
    return redirect("/")