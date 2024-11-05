from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


# class Pizzas(models.Model):
#     name = models.CharField(max_length=250)
#     img = models.FileField(default=None , null=True , upload_to='images')
#     descrip = models.CharField(null=True , max_length=100)
#     prize = models.IntegerField()


# # class Usercart(models.Model):
# #     user = models.OneToOneField(User , on_delete=models.CASCADE , max_length=100 , related_name='usercart' , unique=True)
# #     id = models.UUIDField(default=uuid.uuid4 , editable=False , primary_key=True)

# class Items(models.Model):
#     cart = models.ForeignKey(Usercart , on_delete=models.CASCADE)
#     pizzas = models.ForeignKey(Pizzas , on_delete=models.CASCADE)


