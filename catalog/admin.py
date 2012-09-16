# -*- coding: utf-8 -*-
from django.contrib import admin
from models import CarModel, Category, Colour, Item


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    
class ColourAdmin(admin.ModelAdmin):
    list_display = ('name', 'art')
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('art', 'name', 'category', 'price', 'prepayment', 'stock')

admin.site.register(CarModel, CarAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Item, ItemAdmin)