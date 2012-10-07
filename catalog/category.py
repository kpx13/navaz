# -*- coding: utf-8 -*-

from django.db import models

class Category(models.Model):   # например, передний бампер
    name = models.CharField(max_length=512, verbose_name=u'название')
    image = models.ImageField(upload_to='uploads/categories', max_length=256, null=True, blank=True, verbose_name=u'изображение')

    @staticmethod
    def add_and_get(name):
        name = name.strip()
        if len(name) == 0:
            return
        exists = Category.objects.filter(name=name)
        if len(exists) > 0:
            return exists[0]
        else:
            cm = Category(name=name)
            cm.save()
            return cm
        
    @staticmethod
    def get_name(id_):
        try:
            return Category.objects.get(id=id_).name
        except:
            return None
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering=['name']
    
    def __unicode__(self):
        return self.name