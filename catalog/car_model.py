# -*- coding: utf-8 -*-

from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'название')
    image = models.ImageField(upload_to='car_models', max_length=256, blank=True, verbose_name=u'изображение')
    
    show = models.BooleanField(default=True, verbose_name=u'показывать на сайте?')
    position = models.IntegerField(default=0, blank=True, verbose_name=u'параметр для сортировки')
    
    class Meta:
        verbose_name = 'модель машины'
        verbose_name_plural = 'модели машин'
        ordering=['position']
        
    def __unicode__(self):
        return self.name
