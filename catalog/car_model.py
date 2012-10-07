# -*- coding: utf-8 -*-

from django.db import models

class CarModel(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'название')
    alt_name = models.CharField(max_length=512, blank=True, verbose_name=u'альтернативное название')
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
            return CarModel.objects.get(id=id_).full_name
        except:
            return None
        
    @staticmethod
    def set_alt_name(name, alt_name):
        try:
            cm = CarModel.objects.get(name=name)
            cm.alt_name = alt_name
            cm.save()
        except:
            return None
    
    @property
    def full_name(self):
        name = u'ВАЗ ' + self.name 
        if self.alt_name:
            name = name + u" (%s)" % self.alt_name
        return name
    
    class Meta:
        verbose_name = 'модель машины'
        verbose_name_plural = 'модели машин'
        ordering=['name']
        
    def __unicode__(self):
        return self.name
