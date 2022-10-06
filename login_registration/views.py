from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
            return redirect('customer:index_customer')
        else:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login_registration/login.html')
    else:
        form = AuthenticationForm(request)
        redirect(request, 'login_registration:index', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login_user')


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            user_group = Group.objects.get(name='Customers')   # Agrego el nuevo usuario el grupo Customers
            user.groups.add(user_group)
            messages.success(request, 'Registro de usuario exitoso')
            return render(request, 'login_registration/login.html')
        else:
            messages.error(request, 'Ocurrió un error al crear el usuario')
            form = CustomUserCreationForm()
            return render(request, 'login_registration/registration.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'login_registration/registration.html', {'form': form, })





