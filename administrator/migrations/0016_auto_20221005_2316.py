# Generated by Django 3.2.3 on 2022-10-06 02:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0015_auto_20221005_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateField(default=datetime.datetime(2022, 10, 5, 23, 16, 39, 185281), verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='orderfood',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Cantidad'),
        ),
    ]
