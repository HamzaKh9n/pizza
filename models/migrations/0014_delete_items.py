# Generated by Django 5.0.7 on 2024-10-26 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0013_pizzas_alter_items_pizzas_delete_pizza'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Items',
        ),
    ]