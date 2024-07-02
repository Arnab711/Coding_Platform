from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm
from .models import Message
from .models import Topic
# Create your views here.


@login_required(login_url='login_page')
def index(request):
    topics = Topic.objects.all()  # Retrieve all topics
    context = {'topics': topics}  # Add topics to context
    return render(request, 'index.html', context)

@login_required(login_url='login_page')
def roadmap_page(request):
    return render(request,'roadmap_home.html')

@login_required(login_url='login_page')
def aboutus_page(request):
    return render(request,'aboutus.html')

@login_required(login_url='login_page')
def contact_page(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ob=Message.objects.create(name=name,email=email,message=message)
        return redirect('index')
    return render(request,'contact.html')

def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            us = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            user = authenticate(request,username=us, password=pwd)
            login(request, user)
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login_page')
def restricted_view(request):
    return HttpResponse("This is a restricted view. You are logged in!")


def login_page(request):
    if request.method == 'POST':
        un=request.POST['username']
        pd=request.POST['password']
        user=authenticate(request,username=un,password=pd)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Username or Password is Incorrect')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')

