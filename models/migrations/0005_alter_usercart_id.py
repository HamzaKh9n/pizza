# Generated by Django 5.0.7 on 2024-10-26 15:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_usercart_nothing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
