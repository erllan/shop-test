from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
import random


def generate_code():
    random.seed()
    return str(random.randint(10000, 99999))


def login1(request):
    error = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            error = 'неверная имя или пароль'
    return render(request, 'shop/login.html', {'error': error})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            message = '<a href="localhost:8000/confirm/1">Confirm account</a>'
            send_mail(subject='введите эти числа для потдверждения', message=message, html_message=message,
                      from_email=None,
                      recipient_list=['dpython078@gmail.com'],
                      fail_silently=False)
            return redirect('confirm')
    else:
        return render(request, 'shop/register.html', {'form': form})


def confirm(request):
    if request.method == 'POST':
        pass


def index(request):
    if request.user.is_authenticated:
        return render(request, 'shop/index.html')
    else:
        return redirect('login')
