# Generated by Django 5.0.7 on 2024-10-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_usercart'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='nothing',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]