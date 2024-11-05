# Generated by Django 5.0.7 on 2024-10-26 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0012_delete_cartitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.FileField(default=None, null=True, upload_to='images')),
                ('descrip', models.CharField(max_length=100, null=True)),
                ('prize', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='items',
            name='pizzas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.pizzas'),
        ),
        migrations.DeleteModel(
            name='pizza',
        ),
    ]