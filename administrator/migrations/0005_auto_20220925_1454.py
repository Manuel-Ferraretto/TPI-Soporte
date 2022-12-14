# Generated by Django 3.2.3 on 2022-09-25 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_alter_food_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.AddField(
            model_name='category',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.food', verbose_name='Categoría'),
        ),
        migrations.AddField(
            model_name='pricefood',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.food', verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre'),
        ),
    ]
