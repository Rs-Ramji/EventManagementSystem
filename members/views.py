from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('Login Successfully'))
            return redirect('home')
        else:
            messages.error(request, ('There Was An Error Logging In, Try Again!!'))
            return redirect('login')
    else:
        return render(request, "login.html", {})

def user_logout(request):
    logout(request)
    messages.success(request, ('You Were Logged Out !'))      
    return redirect('login')

def user_registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, ('Registration Successfully'))
            redirect('home')
    else:
        form =  UserCreationForm()
    return render(request, "registration.html", { 'form': form })