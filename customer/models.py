from django.db import models
from administrator.models import Food
import datetime as dt
from django.contrib.auth.models import User

STATES_CHOICES = [
    ('PEND', 'Pendiente'),
    ('ENTR', 'Entregado'),
    ('CANC', 'Cancelado')
]


HOURS_CHOICES = [
    (dt.time(11, 30), '11:30'),
    (dt.time(12, 00), '12:00'),
    (dt.time(12, 30), '12:30'),
    (dt.time(13, 00), '13:00'),
    (dt.time(13, 30), '13:30'),
]

QUANTITIES_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3)
]


class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(verbose_name='Fecha', default=dt.datetime.now())
    state = models.CharField(
        max_length=4,
        choices=STATES_CHOICES,
        default='PEND',
        verbose_name="Estado"
    )
    pickup_time = models.TimeField(
        choices=HOURS_CHOICES,
        default=1,
        verbose_name='Hora de retiro'
    )
    total_price = models.FloatField(verbose_name='Precio Total', default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    items = models.ManyToManyField(Food, related_name='items', through='OrderFood')

    def __str__(self):
        return str(f'Número pedido:{self.id_order} - Usuario: {self.user.first_name} - Estado: {self.state}')


class OrderFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Número de pedido', null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='Comida')
    quantity = models.PositiveIntegerField(
        verbose_name='Elegir cantidad',
        choices=QUANTITIES_CHOICES
    )

    def __str__(self):
        return str(f'Número pedido: {self.order.id_order} - Comida: {self.food.name}')
