from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


def index(request):
    return render(request, 'login_registration/login.html')


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user = user.groups.filter(name='Customers').exists()
            if user:
                return redirect('customer:index_customer')
            else:
                return redirect('administrator:home')
        else:
            messages.error(request, 'Credenciales inválidas')
            return redirect('login_registration:index')
    else:
        form = AuthenticationForm(request)
        redirect('login_registration:index')


def logout_user(request):
    logout(request)
    return redirect('login_registration:index')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user_group = Group.objects.get(name='Customers')   # Agrego el nuevo usuario el grupo Customers
            user.groups.add(user_group)
            messages.success(request, 'Registro de usuario exitoso')
            return redirect('login_registration:index')
        else:
            messages.error(request, 'Ocurrió un error al crear el usuario')
            form = CustomUserCreationForm()
            return render(request, 'login_registration/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'login_registration/registration.html', {'form': form, })





