from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        user_check = User.objects.filter(username = username)

        if user_check.exists():
            messages.info(request,'Username already taken!')
            return redirect("/register")
        
        user = User.objects.create(username = username, first_name = first_name , last_name = last_name, email = email)
        user.set_password(password)
        user.save()
        messages.info(request,"Account created successfully!")
        return redirect('register')

    return render(request,"accounts/register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        print("username is", username)
        password = request.POST.get("password")
        print("password is ", password)

        
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Invalid username!")
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,"Invalid password!")
        else:
            login(request, user)
            return redirect("receipe")
            
    return render(request, "accounts/login.html")

@login_required(login_url = "/login")
def logout_page(request):
    
    logout(request)
    return redirect("/login")