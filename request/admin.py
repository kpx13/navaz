# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_date',)
    search_fields = ('name', 'phone','comment')
    filtered = ('language', )
    ordering = ('-order_date', )
    

admin.site.register(Request, RequestAdmin)
