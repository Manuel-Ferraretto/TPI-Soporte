from django.contrib import admin
from .models import Category, PriceFood, Food

admin.site.register(Category)
admin.site.register(PriceFood)
admin.site.register(Food)
