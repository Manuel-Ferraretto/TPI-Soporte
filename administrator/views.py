from django.shortcuts import render, redirect
from .models import Category, Food
from customer.models import Order
from .forms import CategoryForm, FoodForm
from django.contrib import messages
from django.shortcuts import get_list_or_404


def home(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        return render(request, 'administrator/home.html')


#-------- CRUD Category --------#


def categories(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        all_categories = Category.objects.all()
        return render(request, 'administrator/category.html', {'categories': all_categories})


def create_category(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        form = CategoryForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada con éxito')
            return redirect('administrator:categories')
        return render(request, 'administrator/create_category.html', {'form': form})


def edit_category(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        category = Category.objects.get(id_category=id)
        form = CategoryForm(request.POST or None, instance=category)
        if form.is_valid() and request.POST:
            form.save()
            messages.success(request, 'Cambios realizados con éxito')
            return redirect('administrator:home')
        return render(request, 'administrator/edit_category.html', {'form': form, 'category': category})


def delete_category(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        category = Category.objects.get(id_category=id)
        category.delete()
        messages.success(request, 'Categoría eliminada con éxito')
        return redirect('administrator:categories')


#-------- CRUD Food --------#

def food(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        categories = Category.objects.all()
        all_food = Food.objects.filter(available=True)
        return render(request, 'administrator/food.html', {'food': all_food, 'categories': categories})


def create_food(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        form = FoodForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comida creada con éxito')
            return redirect('administrator:food')
        return render(request, 'administrator/create_food.html', {'form': form})


def edit_food(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        food = Food.objects.get(id_food=id)
        form = FoodForm(request.POST or None, instance=food)
        if form.is_valid() and request.POST:
            form.save()
            messages.success(request, 'Cambios realizados con éxito')
            return redirect('administrator:food')
        return render(request, 'administrator/edit_food.html', {'form': form, 'food': food})


def delete_food(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        food = Food.objects.get(id_food=id)
        food.delete()
        messages.success(request, 'Comida eliminada con éxito')
        return redirect('administrator:food')


#------------------------------------------------------------------#

def orders(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        orders = Order.objects.filter(state='PEND')
        if len(orders) == 0:
            messages.info(request, 'No existen pedidos pendientes')
            return redirect('administrator:home')
        else:
            return render(request, 'administrator/orders.html', {'orders':orders})

def change_order_state(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        order = Order.objects.get(id_order=id)
        order.state = 'ENTR'
        order.save(update_fields=['state'])
        messages.success(request, 'El pedido se entregó con éxito')
        return redirect('administrator:home')



