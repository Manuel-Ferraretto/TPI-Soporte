# Generated by Django 3.2.3 on 2022-09-26 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_auto_20220926_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.category', verbose_name='Categoría'),
        ),
    ]
