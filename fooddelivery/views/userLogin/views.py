from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


def logout_page(request):
    logout(request)
    return redirect('home')


def login_page(request):
    context = {

    }
    username = request.POST.get('username')
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.groups.filter(name__exact="Restaurant").exists():
            return redirect("restaurant_homepage")
        elif user.groups.filter(name__exact="Customer").exists():
            return redirect("home")
        elif user.groups.filter(name__exact="Staff").exists():
            return redirect("home_staff")
    else:
        context['message'] = 'Username or password invalid'
    return render(request, 'fooddelivery/userLogin/home_userLogin.html', context)
