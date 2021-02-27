from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ChangeForm
from .models import Product, User, Category
from django.views import View


def login_user(request):
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


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('confirm')
        else:
            return render(request, 'shop/register.html', {'form': form})
    else:
        return render(request, 'shop/register.html', {'form': form})


def confirm(request):
    if request.method == "GET":
        if request.GET.get('key') is not None:
            user = User.objects.get(key=request.GET.get('key'))
            if user is not None:
                user.is_active = True
                login(request, user)
                user.save()
                return render(request, 'shop/redirect.html')
        else:
            return render(request, 'shop/confirmForm.html')
    else:
        return render(request, 'shop/confirmForm.html')


class Change(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'shop/changeForm.html', )
        else:
            return redirect('login')

    def post(self, request):
        form = ChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            username = User.objects.get(id=request.user.id)
            return HttpResponse(str(username))


def index(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        categories = Category.objects.filter(parent=None)
        return render(request, 'shop/index.html', {'products': products, 'categories': categories})
    else:
        return redirect('login')


def category(request):
    if request.method == "GET":
        category_id = request.GET.get('id')
        category_data = Category.objects.get(id=category_id)
        return render(request, 'shop/category.html', {'category': category_data})


def category_category(request, id):
    category_data = Category.objects.get(id=id)
    return render(request, 'shop/category.html', {'category': category_data})
