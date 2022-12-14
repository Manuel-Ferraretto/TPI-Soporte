# Generated by Django 3.2.3 on 2022-10-05 23:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0014_auto_20221005_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Precio Total'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2022, 10, 5, 20, 56, 18, 924250), verbose_name='Fecha'),
        ),
        migrations.CreateModel(
            name='OrderFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.food', verbose_name='Comida')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.order', verbose_name='Número de pedido')),
            ],
        ),
    ]
