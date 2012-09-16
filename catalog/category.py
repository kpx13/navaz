# -*- coding: utf-8 -*-

from django.db import models

class Category(models.Model):   # например, передний бампер
    name = models.CharField(max_length=512, verbose_name=u'название')
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=u'Родительская категория')
    image = models.ImageField(upload_to='uploads/categories', max_length=256, blank=True, verbose_name=u'изображение')
    
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?')
    position = models.IntegerField(default=0, blank=True, verbose_name=u'параметр для сортировки')
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering=['position']
    
    def __unicode__(self):
        return self.name