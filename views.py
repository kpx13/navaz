# -*- coding: utf-8 -*-

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext
from livesettings import config_value

from request.forms import RequestForm
from pages.models import Page
from news.models import NewsItem
from catalog.models import CarModel, Item, Color, Category
from shop.models import Cart

ADMINS = ['annkpx@gmail.com']

def send_mail_to_admin(data):
    from django.core.mail import send_mail
    text= u'Имя: ' + data['name'] + u"\n" + u'email: ' + data['email'] + '\n' + u'Телефон: ' + data['phone'] + '\n' + u'Текст: ' + data['comment'] + '\n'
    send_mail('Новое сообщение с сайта', text , 'noreply@navaz.ru', ADMINS, fail_silently=False)

def context():
    c = {}
    c['authentication_form'] = AuthenticationForm()
    c['car_models'] = CarModel.objects.all()
    c['colors'] = Color.objects.all()
    c['categories'] = Category.objects.all()
    return c

def get_common_context(request):
    c = context()
    c['request_url'] = request.path
    c['user'] = request.user
    c['authentication_form'] = AuthenticationForm()
    c['car_models'] = CarModel.objects.all()
    c['colors'] = Color.objects.all()
    c['categories'] = Category.objects.all()
    if request.user.is_authenticated():
        c['cart_count'], c['cart_sum'] = Cart.get_goods_count_and_sum(c['user'])
    c.update(csrf(request))
    return c

def view(view_function):
    """ Декоратор """
    
    def wrapped_function(request, *args, **kwargs):
        if request.method == 'POST':
            if request.POST['action'] == 'login':
                if login_user(request, get_common_context(request)):
                    return HttpResponseRedirect('/')
            elif request.POST['action'] == 'logout':
                logout_user(request)
                return HttpResponseRedirect('/')
        return view_function(request, *args, **kwargs)
    
    return wrapped_function


@view
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

@view
def catalog_page(request):
    c = get_common_context(request)
    
    if request.method == 'POST':
        if request.POST['action'] == 'add_in_basket':
            try:
                Cart.add_to_cart(request.user, request.POST['item_id'])
                messages.success(request, u'Товар был добавлен в корзину.')
                return HttpResponseRedirect(request.get_full_path())
            except:
                messages.error(request, u"Перед добавлением товара в корзину необходимо <a href='/accounts/register/'>зарегистрироваться</a>.")
    
    car_model = int(request.GET.get('car_model', '0'))
    category = int(request.GET.get('category', '0'))
    color = int(request.GET.get('color', '0'))
    search = request.GET.get('search', '')
    items = Item.objects.all()
    if car_model:
        items = items.filter(car_model=car_model)
        c['car_model_name'] = CarModel.get_name(car_model)
    if color:
        items = items.filter(color=color)
    if category:
        items = items.filter(category=category)
        c['category_name'] = Category.get_name(category)
    if search:
        items = items.filter(name__icontains=search)
        
    c['car_model'] = car_model
    c['color'] = color
    c['category'] = category
    c['search'] = search
    c['get_request'] = c['request_url'] + "?car_model=%s&category=%s&color=%s&search=%s" % (car_model, category, color, search)
    paginator = Paginator(items, 15)
    page = int(request.GET.get('page', '1'))
    try:
        c['items'] = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        c['items'] = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        c['items'] = paginator.page(page)
    c['page'] = page
    c['page_range'] = paginator.page_range
    if len(c['page_range']) > 1:
        c['need_pagination'] = True
    return render_to_response('catalog.html', c, context_instance=RequestContext(request))

@view
def cart_page(request):
    c = get_common_context(request)
    if request.method == 'POST':
        if request.POST['action'] == 'del_from_basket':
            Cart.del_from_cart(request.user, request.POST['item_id'])
            messages.success(request, u'Товар был удален из корзины.')
            return HttpResponseRedirect(request.get_full_path())
        elif request.POST['action'] == 'change_count':
            Cart.change_count(request.user, request.POST['item_id'], request.POST['item_count'])
            messages.success(request, u'Количество единиц товара было изменено.')
            return HttpResponseRedirect(request.get_full_path())
    
    
    c['items'] = Cart.get_content(request.user)
    return render_to_response('cart.html', c, context_instance=RequestContext(request))

@view
def order_page(request):
    c = get_common_context(request)
    return render_to_response('order.html', c, context_instance=RequestContext(request))

@view
def item_page(request, item_id):
    if request.method == 'POST':
        if request.POST['action'] == 'add_in_basket':
            try:
                Cart.add_to_cart(request.user, request.POST['item_id'])
                messages.success(request, u'Товар был добавлен в корзину.')
            except:
                messages.error(request, u"Перед добавлением товара в корзину необходимо <a href='/accounts/register/'>зарегистрироваться</a>.")
    c = get_common_context(request)
    c['item'] = Item.get(item_id)
    return render_to_response('item.html', c, context_instance=RequestContext(request))

@view
def request_page(request):
    c = get_common_context(request)
    if request.method == 'GET':
        c['request_form'] = RequestForm()
    else:
        form = RequestForm(request.POST)
        if form.is_valid():
            send_mail_to_admin(form.cleaned_data)
            form.save()
            form = RequestForm()
            messages.success(request, u'Ваш запрос отправлен.')
            return HttpResponseRedirect('/')
        else:
            c['request_form'] = form
    return render_to_response('request.html', c, context_instance=RequestContext(request))

@view
def other_page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_page_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        return HttpResponseNotFound('page not found')
        #return render_to_response('base.html', c, context_instance=RequestContext(request))

def login_user(request, c):
    form = AuthenticationForm(request.POST)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            messages.success(request, u'Вы успешно вошли на сайт.')
            return True
        else:
            c['authentication_form'] = form
            messages.error(request, u'Ваш аккаунт не активирован.')
            return False
    else:
        c['authentication_form'] = form
        messages.error(request, u'Неверный логин или пароль.')
        return False


def logout_user(request):
    auth.logout(request)
