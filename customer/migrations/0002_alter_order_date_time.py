# Generated by Django 3.2.3 on 2022-11-12 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 12, 19, 22, 5, 121340), verbose_name='Fecha'),
        ),
    ]
