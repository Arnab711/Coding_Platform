from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.


@login_required(login_url='login_page')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login_page')
def roadmap_page(request):
    return render(request,'roadmap_home.html')

@login_required(login_url='login_page')
def aboutus_page(request):
    return render(request,'aboutus.html')

@login_required(login_url='login_page')
def contact_page(request):
    return render(request,'contact.html')

def register_page(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
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

