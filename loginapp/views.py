from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages




def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')

        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        return redirect('logins')

    return render(request, 'signup.html')

def logins(request):
    

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            
            return render(request,"index.html")
        else:
            return HttpResponse('signup')


    return render(request,'login.html')

def home(request):
    return HttpResponse('home')