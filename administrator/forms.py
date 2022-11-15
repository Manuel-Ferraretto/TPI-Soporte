from django import forms
from .models import Category, Food


# A través de los forms después Django genera el template

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'      # Se incluyen todos los campos del modelo


class FoodForm(forms.ModelForm):
    category = forms.ModelChoiceField(              #Crea un dropdown con todas las categorías
                queryset=Category.objects.all(),
                initial=0,
                label='Seleccione una categoría',
                )

    class Meta:
        model = Food
        fields = ['name', 'description', 'available', 'category', 'price']  # Se aclara los campos que se incluyen



