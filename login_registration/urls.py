from django.urls import path
from login_registration import views

app_name = 'login_registration'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
]