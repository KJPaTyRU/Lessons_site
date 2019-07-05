from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import forms

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'main/login.html', context={'failure':True,
                                                               'form':form})

    # creating login form
    return render(request, 'main/login.html', context={'form':form})



def register(request):
    # creating register form and saving new user in db
    form = forms.RegisterForm()
    if request.user.is_authenticated:
        return render(request, 'main/register.html', context={'auth':True})
    else:
        if request.method == "POST":
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user = User.objects.create_user(username, password=password1)
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'main/register.html', context={'failure': True,
                                                                   'form': form})

        return render(request, 'main/register.html', {'form':form})




# hi