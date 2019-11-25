from django.shortcuts import render, redirect
from . import post
from django.http import HttpResponse
from . import signup
from . models import Post, SignUpForm



# Create your views here.

def landing(request):
    return render(request,'landingpage.html')

def home(request):
    return HttpResponse("Hello")


def about(request):
    return render(request,'about.html')

def login(request):
    dict={'name':"This is a Login Page! Please enter your details below"}
    return render(request,'firstapp/login.html',context=dict)

def welcome(request):
    dict={'welcome':"Congratulations! You are signed in"}
    return render(request,'firstapp/login_welcome.html',context=dict)


'''
def signup_view(request):
    form=signup.SignupForm

    if request.method=="POST":
        form=signup.SignupForm(request.POST)
        if form.is_valid():
            print("Validation Worked")
            print("First Name: "+ form.cleaned_data['firstname'])
            print("Last Name: " + form.cleaned_data['lastname'])
            print("Password: " + form.cleaned_data['password'])
            print("Re-Entered Password: " + form.cleaned_data['repassword'])


    return render(request,'firstapp/signup.html',{'signuptag':form})
    '''

def signup_view(request):
    form=signup.SignupForm

    if request.method=="POST":
        form=signup.SignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/logintask3')
            except:
                pass
    else:
        form=signup.SignupForm
        return render(request,'firstapp/signup.html',{'signuptag':form})

def success(request):



    return render(request,'firstapp/logintask3.html')





def post(request):
    form = signup.PostForm(request.POST)
    if request.method == "POST":
        form = signup.PostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = signup.PostForm()
    return render(request,'index.html',{'form':form})


def show(request):
    posts = Post.objects.all()
    return render(request,"show.html",{'posts':posts})


def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request,'edit.html', {'post':post})


def update(request, id):
    post = Post.objects.get(id=id)
    form = signup.PostForm(request.POST, instance = post)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'post': post})



def destroy(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/show")


def logout(request):
    return redirect("/logintask3")