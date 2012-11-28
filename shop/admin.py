# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'count', 'date')
    search_fields = ('item', )

admin.site.register(Cart, CartAdmin)