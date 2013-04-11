# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from catalog.item import Item


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', verbose_name=u'пользователь')
    fio = models.CharField(max_length=256, verbose_name=u'ФИО')    
    phone = models.CharField(max_length=20, verbose_name=u'телефон')
    favorites = models.ManyToManyField(Item, blank=True, verbose_name=u'избранное')

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'
    
    def __unicode__ (self):
        return str(self.user.username)
    
    def favorites_check(self, item):
        return (Item.get(item) in self.favorites.all())
    
    def add_to_favorites(self, item):
        self.favorites.add(item)
        
    def del_favorites(self, item):
        self.favorites.remove(item)
    
    def get_items(self):
        return self.favorites.all()
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    

class RobokassaOperation(models.Model):
    user = models.ForeignKey(User, verbose_name=u'пользователь')
    time = models.DateTimeField(auto_now=True, verbose_name=u'время')
    value = models.FloatField(verbose_name=u'сумма')
    comment = models.TextField(blank=True, verbose_name=u'статус - комментарий менеджера')
    done = models.BooleanField(blank=True, default=False, verbose_name=u'операция завершена успешно')
    history = models.TextField(blank=True, verbose_name=u'история')
    
    class Meta:
        verbose_name = u'запись на ввод денег'
        verbose_name_plural = u'ввод денег'
        ordering=('-time',)

    @staticmethod
    def create(user, value):
        op = RobokassaOperation(value=value, user=user, done=False)
        op.history = u'Платежка создана.<br />'
        op.save()
        return op.id
    
    @staticmethod
    def check_user_and_id(user, id):
        try:
            op = RobokassaOperation.objects.get(id=id)
        except:
            return False
        return True
        #return op.user == user
    
    @staticmethod
    def get_by_id(id):
        try:
            return RobokassaOperation.objects.get(id=id)
        except:
            return False

        
    @staticmethod
    def end_with_error(user, id):
        if not RobokassaOperation.check_user_and_id(user, id):
            return False
        op = RobokassaOperation.objects.get(id=id)
        op.history  = op.history + u'Платеж не был завершен.<br />'
        op.save()
        return True
        
    @staticmethod
    def end_with_success(user, id):
        if not RobokassaOperation.check_user_and_id(user, id):
            return False
        op = RobokassaOperation.objects.get(id=id)
        if not op.done:
            op.history  = op.history + u'Платеж завершен успешно.<br />'
            op.done = True
            op.save()
            op.user.get_profile().earn(op.value, u'Платеж через Робокассу.')
        return True