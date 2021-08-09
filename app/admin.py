from app.models import Menu, Order, Restaurant
from django.contrib import admin
from .models import *
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','restaurant_name','items','price']
    filter = ['restaurant_name','items']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact','address']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_contact', 'user_email', 'user_address', 'item_name','restaurant_name']
    

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(User)