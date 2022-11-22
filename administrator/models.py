from django.db import models


class Category(models.Model):
    id_category = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=45, verbose_name="Nombre", unique=True)  # verbose_name es para que diga "Nombre" en vez de name

    class Meta:
        ordering = ['name']

    def __str__(self):          # Devuelve nombre de la categoría así cuando lo imprimís se ve el nombre
        return self.name        # Ejemplo: en el admin site en vez de decir Object(1) va a decir el nombre de la categoría


class Food(models.Model):
    id_food = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, verbose_name="Nombre", unique=True)
    description = models.CharField(max_length=100, verbose_name="Descripción")
    available = models.BooleanField(verbose_name="Disponible")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Seleccione la categoría")
    price = models.FloatField(verbose_name="Precio")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # Redefinición del método Save() para que cuando se guarda la instancia, redonde a 2 decimales
        self.price = round(self.price, 2)
        super(Food, self).save(*args, **kwargs)
