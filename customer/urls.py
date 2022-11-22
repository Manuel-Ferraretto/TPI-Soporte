from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('order/index', views.index_order, name='index_order'),
    path('order/index_customer', views.index_customer, name='index_customer'),
    path('order/create', views.create_order, name='create_order'),
    path('order/create_order_food<int:id>', views.create_order_food, name='create_order_food'),
    path('order/show_cart', views.show_cart, name='show_cart'),
    path('order/delete_item<int:id>', views.delete_item_from_cart, name='delete_from_cart'),
    path('order/send_order', views.send_order, name='send_order'),
    path('order/view_all_orders', views.view_all_orders, name='view_all_orders'),
    path('order/view_pending_order', views.view_pending_order, name='view_pending_order'),
    path('order/clean_cart', views.clean_cart, name='clean_cart'),
    path('order/cancel_order<int:id>', views.cancel_order, name='cancel_order'),

]