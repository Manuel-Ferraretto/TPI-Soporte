from django.urls import path
from administrator import views

app_name = 'administrator'    # Agrega nombre a la aplicación para que no haya errores al hacer redirect a una url
                              # nombre_aplicación:name_url

urlpatterns = [
    path('administrator/', views.home, name='home'),

    path('category/categories', views.categories, name='categories'),
    path('category/create', views.create_category, name='create_category'),
    path('category/edit/<int:id>', views.edit_category, name='edit_category'),
    path('category/delete/<int:id>', views.delete_category, name='delete_category'),

    path('food/food', views.food, name='food'),
    path('food/create', views.create_food, name='create_food'),
    path('food/edit/<int:id>', views.edit_food, name='edit_food'),
    path('food/delete/<int:id>', views.delete_food, name='delete_food'),

    path('order/pending_orders', views.orders, name='pending_orders'),
    path('food/change_state/<int:id>', views.change_order_state, name='change_state'),

]
