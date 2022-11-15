from django.contrib import admin
from .models import Category, Food

admin.site.register(Category)
#admin.site.register(PriceFood)
admin.site.register(Food)
