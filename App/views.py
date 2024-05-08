from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):

    return render(request, 'home.html')
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else: 
            return HttpResponse("Username or Password is incorrect")
        
    return render(request, 'login.html')
    # template = loader.get_template('login.html')
    # return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username__iexact=uname).exists():
            return HttpResponse("Username already exists")
        elif User.objects.filter(email__iexact=email).exists():
            return HttpResponse("Email already exists")
        elif password1 == password2:
            user = User.objects.create_user(uname, email, password1)
            user.save()
            return redirect('login')
        
    return render(request, 'signup.html')
    # template = loader.get_template('signup.html')
    # return HttpResponse(template.render())

def signout(request):
    logout(request)
    return redirect('login')
