# -*- coding: utf-8 -*-

from django.db import models

from car_model import CarModel
from category import Category

class Color(models.Model):
    name = models.CharField(max_length=512, verbose_name=u'название')
    art = models.CharField(max_length=512, verbose_name=u'номер')
    code = models.CharField(max_length=10, blank=True, verbose_name=u'grb-код')
    
    @staticmethod
    def add_and_get(name):
        name = name.strip()
        if len(name) == 0:
            return
        exists = Color.objects.filter(name=name)
        if len(exists) > 0:
            return exists[0]
        else:
            cm = Color(name=name)
            cm.save()
            return cm
    
    class Meta:
        verbose_name = 'цвет'
        verbose_name_plural = 'цвета'
        ordering=['name']

    def __unicode__(self):
        return self.name
    
class Item(models.Model):   # задний бампер, цвет персей, на ВАЗ 2113, полноокрашенный
    category = models.ForeignKey(Category, verbose_name=u'категория')
    car_model = models.ForeignKey(CarModel, verbose_name=u'модель авто')
    color = models.ForeignKey(Color, null=True, blank=True, verbose_name=u'цвет')
    name = models.CharField(max_length=512, verbose_name=u'название')
    art = models.CharField(max_length=16, blank=True, verbose_name=u'артикул')
    price = models.FloatField(verbose_name=u'цена')
    profit = models.FloatField(verbose_name=u'профит')
    prepayment = models.FloatField(verbose_name=u'предоплата', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/items', max_length=256, blank=True, verbose_name=u'изображение')
    description = models.TextField(default=u'У товара нет подробного описания.', verbose_name=u'описание')
    stock = models.IntegerField(default=0, verbose_name=u'в наличии')

    @staticmethod
    def get(id_):
        try:
            return Item.objects.get(id=id_)
        except:
            return None
    
    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering=['name']
        
    def __unicode__(self):
        return self.name