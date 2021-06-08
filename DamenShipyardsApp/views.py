from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def index_home_view(request, *args, **kwargs):
    return render(request, "Home/index.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, "Login/login.html", {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
