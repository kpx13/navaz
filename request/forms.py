# -*- coding: utf-8 -*-
 
from django.forms import ModelForm
from models import Request
        
class RequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ('order_date', )
