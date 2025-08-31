from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User  # Use your custom User model if any
from django.contrib import messages
from django.http import HttpResponse

def users_home(request):
    return render(request, "users/home.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Simple user creation (improve later)
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('job_list')  # redirect to job list after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
