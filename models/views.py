from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def home(request):
    if User.is_authenticated:
        msg = 'Logout'
    else:
        msg = 'Login'
    data = Pizzas.objects.all()
    return render(request , "home.html" , {'pizza' : data , 'msg':msg}) 

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username , email = email , password = password)
        if request.user is not None:
            login(request , user)
            return redirect('home')
        else:
            return HttpResponse("Incorrest email or password")
    return render(request , 'Auth/login.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username , email , password)
        user.save()
        print(email , password , 'success')
    return render(request , 'Auth/signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def cart(request):
    something = Usercart.objects.get(user = request.user)
    if something is not None:
        return render(request , 'cart.html' , {'user':request.user})
    else:
        myuser = request.user
        b = Usercart(user = myuser)
        b.save()
        print('success')
        return render(request , 'cart.html' , {'user':request.user})
