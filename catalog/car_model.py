# -*- coding: utf-8 -*-

from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'название')
    image = models.ImageField(upload_to='car_models', max_length=256, null=True, blank=True, verbose_name=u'изображение')
    
    @staticmethod
    def add_and_get(name):
        name = name.strip()
        if len(name) == 0:
            return
        exists = CarModel.objects.filter(name=name)
        if len(exists) > 0:
            return exists[0]
        else:
            cm = CarModel(name=name)
            cm.save()
            return cm
    
    @staticmethod
    def get_name(id_):
        try:
            return CarModel.objects.get(id=id_).name
        except:
            return None
        
    
    class Meta:
        verbose_name = 'модель машины'
        verbose_name_plural = 'модели машин'
        ordering=['name']
        
    def __unicode__(self):
        return self.name
