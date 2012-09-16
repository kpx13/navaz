# -*- coding: utf-8 -*-
from django.db import models
import datetime

class NewsItem(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'Название')
    date = models.DateTimeField(default=datetime.datetime.now, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст')
    position = models.IntegerField(blank=True, default = 100, verbose_name=u'Позиция в списке')
    
    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ['-position']
        
    def __unicode__(self):
        return self.name
    