# Generated by Django 5.0.7 on 2024-10-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='descrip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
