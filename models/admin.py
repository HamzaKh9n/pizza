from django.contrib import admin
from .models import *

class pizza_dis(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'img']
    
# Register your models here.

# # admin.site.register(Pizzas)
# admin.site.register(Usercart)