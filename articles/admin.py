# -*- coding: utf-8 -*-
from django.contrib import admin
from models import NewsItem

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'position')
    search_fields = ('name', 'text')

admin.site.register(NewsItem, NewsAdmin)