# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
import datetime

from catalog.item import Item

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Юзер')
    item = models.ForeignKey(Item, verbose_name=u'Товар')
    count = models.IntegerField(default=1, verbose_name=u'Количество')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'Дата добавления')
    
    
    class Meta:
        verbose_name = u'товар в корзине'
        verbose_name_plural = u'товары в корзине'
        ordering = ['-date']
        
    def __unicode__(self):
        return self.item.name
    
    @staticmethod
    def add_to_cart(user, item_id, count=1):
        alr = Cart.objects.filter(item=item_id)
        if len(alr) == 0:
            Cart(user=user, item=Item.get(item_id), count=count).save()
        else:
            alr[0].count = alr[0].count + count
            alr[0].save()
    
    @staticmethod
    def change_count(user, item_id, count):
        alr = Cart.objects.filter(item=item_id)
        if count < 0:
            return
        if len(alr) == 0:
            Cart(user=user, item=Item.get(item_id), count=count).save()
            if count == 0:
                Cart.objects.filter(item=item_id).delete()
        else:
            alr[0].count = count
            alr[0].save()
            
    @staticmethod
    def del_from_cart(user, item_id):
        alr = Cart.objects.filter(item=item_id)
        if len(alr) == 0:
            return
        else:
            Cart.objects.filter(item=item_id).delete()
    
    @staticmethod
    def get_content(user):
        cart = list(Cart.objects.filter(user=user))
        return cart
    
    @staticmethod
    def get_goods_count_and_sum(user):
        cart = Cart.get_content(user)
        return (len(cart), sum([x.count * x.item.price for x in cart]))
    

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=u'Юзер')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'Дата заказа')
    
    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'
        ordering = ['-date']
        
    def __unicode__(self):
        return self.date
    
    
    
    
    