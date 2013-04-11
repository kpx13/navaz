# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import UserProfile, RobokassaOperation

class UserProfileInline(admin.StackedInline): 
    model = UserProfile
    extra = 1

class ExtUserAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
    list_display = UserAdmin.list_display + ('is_active',)



admin.site.unregister(User)
admin.site.register(User, ExtUserAdmin)
admin.site.register(RobokassaOperation)