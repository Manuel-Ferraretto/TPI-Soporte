# Generated by Django 3.2.3 on 2022-09-25 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_alter_category_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.category', verbose_name='Categoría'),
        ),
    ]