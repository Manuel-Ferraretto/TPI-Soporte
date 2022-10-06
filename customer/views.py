from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order, OrderFood
from administrator.models import Category, Food
from .forms import OrderForm, OrderFoodForm
from django.contrib.auth.decorators import login_required


def index_customer(request):
    return render(request, 'customer/menu_customer.html')


def index_order(request):
    categories = Category.objects.all()
    all_food = Food.objects.filter(available=True)
    return render(request, 'customer/choose_category.html', {'food': all_food, 'categories': categories})


def create_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_order')
    else:
        return render(request, 'customer/create_order.html', {'form': form})


def add_to_order(request, id):
    pass
