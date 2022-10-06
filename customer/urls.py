from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('order/index', views.index_order, name='index_order'),
    path('order/index_customer', views.index_customer, name='index_customer'),
    path('order/create', views.create_order, name='create_order'),
    path('order/add_to_order', views.add_to_order, name='add_to_order'),

]