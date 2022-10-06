from django.shortcuts import render, redirect
from .models import Category, Food, PriceFood
from .forms import CategoryForm, FoodForm
from django.contrib import messages
from django.shortcuts import get_list_or_404


def home(request):
    return render(request, 'administrator/home.html')


#-------- CRUD Category --------#


def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'administrator/category.html', {'categories': all_categories})


def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('administrator:categories')
    return render(request, 'administrator/create_category.html', {'form': form})


def edit_category(request, id):
    category = Category.objects.get(id_category=id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('administrator:home')
    return render(request, 'administrator/edit_category.html', {'form': form, 'category': category})


def delete_category(request, id):
    category = Category.objects.get(id_category=id)
    category.delete()
    return redirect('administrator:categories')


#-------- CRUD Food --------#

def food(request):
    categories = Category.objects.all()
    all_food = Food.objects.filter(available=True)
    return render(request, 'administrator/food.html', {'food': all_food, 'categories': categories})


def create_food(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('administrator:food')
    return render(request, 'administrator/create_food.html', {'form': form})


def edit_food(request, id):
    food = Food.objects.get(id_food=id)
    form = FoodForm(request.POST or None, instance=food)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('administrator:food')
    return render(request, 'administrator/edit_food.html', {'form': form, 'food': food})


def delete_food(request, id):
    food = Food.objects.get(id_food=id)
    food.delete()
    return redirect('administrator:food')






