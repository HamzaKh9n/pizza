# Generated by Django 5.0.7 on 2024-10-26 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_alter_usercart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='model_id',
        ),
    ]