# -*- coding: utf-8 -*-

from django.contrib.auth.models import User


def add_user(name, email, password, phone, work_phone, type, balance=0.0):
    u = User(username=email)
    u.set_password(password)
    u.save()
    p = u.get_profile()
    p.phone = phone
    p.work_phone=work_phone
    p.type=type
    p.balance = balance
    p.fio = name
    p.save()
    return u

