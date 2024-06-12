from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render (request,'index.html')

def aboutus(request):
    return render (request,'about.html')

def services(request):
    return render (request,'services.html')

def career(request):
    return render (request,'career.html')

def signup(request):
     if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use')
            return redirect('/consultancyproject/signup.html/')
        else:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            return redirect('/')
    #     User.objects.create_user(username=name,email=email,password=password)
    #     return redirect('/')
     else:
         return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        # email=request.POST['email']
        username=request.POST['name']
        password=request.POST['password']
		
        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            return redirect('index.html')
    else:
        return render(request,'login.html')
	

def contactus(request):
    return render (request,'contact.html')


