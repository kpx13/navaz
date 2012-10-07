# -*- coding: utf-8 -*-
from django.db import models
import datetime

class NewsItem(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'Название')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'Дата')
    text = models.TextField(verbose_name=u'Текст')
    
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-date']
        
    def __unicode__(self):
        return self.name
    