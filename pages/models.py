# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=256, verbose_name=u'заголовок')
    content = RichTextField(verbose_name=u'контент')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, help_text=u'Изменять не рекомендуется.')
    
    @classmethod
    def get_page_by_slug(cls, page_name):
        try:
            page = cls.objects.get(slug=page_name)
            return {'title': page.title,
                    'content': page.content}
        except:
            return None
        
    
    class Meta:
        verbose_name = u'статическая страница'
        verbose_name_plural = u'статические страницы'
        
    def __unicode__(self):
        return self.slug