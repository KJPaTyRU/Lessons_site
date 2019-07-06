from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            from django.db import IntegrityError;
            try:
                user = User.objects.create_user(username, password=password1)
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'main/register.html', context={'user_failure': True,
                                                                      'username': username,
                                                                      'form': form})
        else:
            return render(request, 'main/register.html', context={'pas_failure': True,
                                                               'form': form})

    return render(request, 'main/register.html', {'form':form})

@login_required
def kingdom(request):
    return render(request, 'main/kingdom.html')


@login_required
def logout_page(request):
    logout(request)
    return redirect("/")


def send_m(request):
    header = "Privet, Steave!"
    content = "Testing API"
    author = "druidmasterbro@gmail.com"
    reciver = ["lzdragonmens@gmail.com"]

    send_mail(header, content, author, reciver, fail_silently=False)

    return redirect('/')
# hi