# Generated by Django 3.2.3 on 2022-09-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id_category',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='food',
            name='id_food',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]