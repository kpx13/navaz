# -*- coding: utf-8 -*-
from django.db import models

class Request(models.Model):
    name = models.CharField(u'Имя', max_length=256)
    email = models.EmailField(u'E-mail', blank=True, max_length=256)
    phone = models.CharField(u'Телефон', blank=True, max_length=256)
    comment = models.TextField(u'Сообщение', blank=True)
    order_date = models.DateTimeField(u'Время заказа', auto_now_add=True)

    class Meta:
        verbose_name = u'сообщение'
        verbose_name_plural = u'сообщения'
        ordering = ['-order_date']

    def __unicode__(self):
        return self.name
