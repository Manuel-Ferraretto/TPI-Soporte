from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order, OrderFood
from administrator.models import Category, Food
from .forms import OrderForm, OrderFoodForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

cart = []
order = Order()


def index_customer(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        current_user = User.objects.get(id = request.user.id)
        return render(request, 'customer/menu_customer.html', {'current_user':current_user})


def create_order(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        orders = Order.objects.filter(user=request.user)
        flag=False
        for i in orders:
            if i.state == 'PEND':
                flag=True
                break
        if not flag:
            if len(cart) == 0:
                form = OrderForm(request.POST or None)
                if form.is_valid():
                    order.user = User.objects.get(id = request.user.id)
                    order.pickup_time = form.cleaned_data['pickup_time']
                    order.date_time = datetime.now()
                    #order.save()
                    return redirect('customer:index_order')
                else:
                    return render(request, 'customer/create_order.html', {'form':form})
            else:
                return redirect('customer:index_order')
        else:
            messages.info(request, 'El usuario ya tiene un pedido pendiente')
            return redirect('customer:index_customer')


def index_order(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        categories = Category.objects.all()
        all_food = Food.objects.filter(available=True)
        return render(request, 'customer/choose_food.html', {'food': all_food, 'categories': categories})


def create_order_food(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        form = OrderFoodForm(request.POST or None)
        item = Food.objects.get(id_food=id)
        flag = False
        for c in cart:                #Verifico que el item no se haya agregado anteriormente
            if c.food == item:
                flag = True
                break

        if not flag:
            if form.is_valid():
                order_food = OrderFood()
                order_food.food = item
                order_food.quantity = form.cleaned_data['quantity']
                cart.append(order_food)
                messages.success(request, 'Item agregado con éxito al pedido')
                return redirect('customer:index_order')
            else:
                return render(request, 'customer/add_to_order.html', {'form':form, 'item': item})
        else:
            messages.warning(request, 'El item ya fue agregado al pedido')
            return redirect('customer:index_order')


def show_cart(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        total_price = 0
        for item in cart:
            total_price += item.food.price * item.quantity
        order.total_price = total_price
        orders = Order.objects.filter(user=request.user)
        flag=False
        for i in orders:                  
            if i.state == 'PEND':
                flag=True
                break
        if flag:
            return render(request, 'customer/view_pending_order.html', {'cart': cart, 'total_price':total_price}) 
        elif len(cart) == 0:
            messages.info(request, 'No hay productos agregados al pedido')
            return redirect('customer:index_customer')
        else:
            return render(request, 'customer/cart.html', {'cart': cart, 'total_price':total_price})


def delete_item_from_cart(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        item = Food.objects.get(id_food=id)
        order_food = OrderFood.objects.get(food=item)
        cart.remove(order_food)
        if len(cart) == 0:
            return redirect('customer:index_order')
        else:
            return render(request, 'customer/cart.html', {'cart':cart})


def send_order(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        order.save()
        for order_food in cart:
            order_food.order = order
            order_food.save()
            order.total_price += order_food.food.price
        messages.success(request, 'Pedido enviado con éxito')
        return redirect('customer:index_customer')


def view_all_orders(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        orders = Order.objects.filter(user=request.user).order_by('-date_time')
        return render(request, 'customer/all_orders.html', {'orders':orders})

def view_pending_order(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        try:
            order = Order.objects.get(user=request.user, state='PEND')
            items = OrderFood.objects.filter(order=order)
            total_price = 0
            for i in items:
                total_price += i.food.price
            return render(request, 'customer/view_pending_order.html', {'order':order, 'items':items, 'total_price':total_price})
        except:
            messages.info(request, 'No existen pedidos pendientes')
            return redirect('customer:index_customer')
    


def cancel_order(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión')
        return redirect('login_registration:index')
    else:
        order = Order.objects.get(id_order=id)
        order.delete()
        messages.success(request, 'El pedido fue cancelado con éxito')
        return redirect('customer:index_customer')


def clean_cart(request):
    cart.clear()
    return redirect('login_registration:logout')