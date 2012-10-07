# -*- coding: utf-8 -*-

from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext

from request.forms import RequestForm
from pages.models import Page
from news.models import NewsItem
from catalog.models import CarModel, Item, Colour, Category

def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['car_models'] = CarModel.objects.all()
    c['colors'] = Colour.objects.all()
    c['categories'] = Category.objects.all()
    c.update(csrf(request))
    return c

def home_page(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['about'] = Page.get_page_by_slug('home_about')['content']
    c['delivery'] = Page.get_page_by_slug('home_delivery')['content']
    c['catalog'] = Page.get_page_by_slug('home_catalog')['content']
    c['warranty'] = Page.get_page_by_slug('home_warranty')['content']
    c['sale'] = Page.get_page_by_slug('home_sale')['content']
    c['news'] = NewsItem.objects.all()
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def catalog_page(request):
    c = get_common_context(request)
    items = Item.objects.all()
    paginator = Paginator(items, 15)
    page = request.GET.get('page', '1')
    try:
        c['items'] = paginator.page(page)
    except PageNotAnInteger:
        c['items'] = paginator.page(1)
    except EmptyPage:
        c['items'] = paginator.page(paginator.num_pages)
    
    return render_to_response('catalog.html', c, context_instance=RequestContext(request))

def request_page(request):
    c = get_common_context(request)
    if request.method == 'GET':
        c['request_form'] = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            form = RequestForm()
            messages.success(request, u'Ваш запрос отправлен.')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, u'Возникла ошибка при отправлении сообщения.')
    return render_to_response('request.html', c, context_instance=RequestContext(request))

def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_page_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        #return HttpResponseNotFound('page not found')
        return render_to_response('base.html', c, context_instance=RequestContext(request))


def insert_test_data(request):
    import test_data
    test_data.go_pages()
    test_data.go_news()
    return HttpResponseRedirect('/')
