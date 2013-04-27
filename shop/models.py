# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Template

from catalog.item import Item

def sendmail(subject, body):
    mail_subject = ''.join(subject)
    send_mail(mail_subject, body, settings.DEFAULT_FROM_EMAIL,
        settings.SEND_ALERT_EMAIL)

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=u'пользователь')
    item = models.ForeignKey(Item, verbose_name=u'товар')
    count = models.IntegerField(default=1, verbose_name=u'количество')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'дата добавления')
    
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
    def update(user, dict_):
        for d in dict_:
            Cart(user=user, item=d['item'], count=d['count']).save()
    
    @staticmethod
    def count_plus(user, item_id):
        alr = Cart.objects.filter(item=item_id)[0]
        alr.count += 1 
        alr.save()
    
    @staticmethod
    def count_minus(user, item_id):
        alr = Cart.objects.filter(item=item_id)[0]
        if alr.count <= 1:
            alr.delete()
            return
        alr.count -= 1 
        alr.save()
            
    @staticmethod
    def del_from_cart(user, item_id):
        alr = Cart.objects.filter(item=item_id)
        if len(alr) == 0:
            return
        else:
            Cart.objects.filter(item=item_id).delete()
    
    @staticmethod    
    def clear(user):
        Cart.objects.filter(user=user).delete()
    
    @staticmethod
    def get_content(user):
        cart = list(Cart.objects.filter(user=user))
        return cart
    
    @staticmethod
    def get_goods_count_and_sum(user):
        cart = Cart.get_content(user)
        return (sum([x.count for x in cart]), sum([x.count * x.item.price for x in cart]))



class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=u'пользователь')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'дата заказа')
    comment = models.TextField(blank=True, verbose_name=u'комментарий')
    
    class Meta:
        verbose_name = u'заказ'
        verbose_name_plural = u'заказы'
        ordering = ['-date']
    
    def __unicode__(self):
        return str(self.date)
    
    def get_count(self):
        return sum([x.count for x in OrderContent.get_content(self)])
    
    def get_sum(self):
        return sum([x.count * x.item.price for x in OrderContent.get_content(self)])
    
    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        OrderContent.move_from_cart(self.user, self)
        subject=u'Поступил новый заказ с сайта NaVaz.ru',
        body_templ=u"""Пользователь: http://navaz.ru/admin/auth/user/{{ o.user.id }}/ 
Содержимое:
    {% for c in o.content.all %}
        Товар: http://navaz.ru/item/{{ c.item.id }}, {{ c.count }} шт. по цене {{ c.item.price }} руб.
    {% endfor %}
Всего позиций: {{ o.get_count }} шт.
Общая стоимость:  {{ o.get_sum }} руб. 
Сообщение: {{ o.comment }}
"""
        body = Template(body_templ).render(Context({'o': self}))
        sendmail(subject, body)    
        
class OrderContent(models.Model):
    order = models.ForeignKey(Order, verbose_name=u'заказ', related_name='content')
    item = models.ForeignKey(Item, verbose_name=u'товар')
    count = models.IntegerField(default=1, verbose_name=u'количество')
        
    def __unicode__(self):
        return self.item.name
    
    @staticmethod
    def add(order, item, count):
        OrderContent(order=order, item=item, count=count).save()
        
    @staticmethod
    def move_from_cart(user, order):
        cart_content = Cart.get_content(user)
        for c in cart_content:
            OrderContent.add(order, c.item, c.count)
        Cart.clear(user) 
        
    @staticmethod
    def get_content(order):
        return list(OrderContent.objects.filter(order=order))
    