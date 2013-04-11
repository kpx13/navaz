# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Cart, Order

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'count', 'date')
    search_fields = ('item', )
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    search_fields = ('user', )

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)