# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Cart, Order, OrderContent

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'count', 'date')
    search_fields = ('item', )
    
class OrderInline(admin.StackedInline): 
    model = OrderContent
    extra = 3
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline, ]
    list_display = ('user', 'date')
    search_fields = ('user', )

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)