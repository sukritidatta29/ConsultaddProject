from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello")


def about(request):
    return HttpResponse("About Page")

def login(request):
    dict={'name':"This is a Login Page! Please enter your details below"}
    return render(request,'firstapp/login.html',context=dict)

def welcome(request):
    dict={'welcome':"Congratulations! You are signed in"}
    return render(request,'firstapp/login_welcome.html',context=dict)