# -*- coding: utf-8 -*-

from pages.models import Page
from news.models import NewsItem

def go_pages():
    Page.objects.all().delete()

    Page(slug='home_about', title=u'О компании на главной', content=u"""<p>Sed placerat accumsan ligula. Aliquam felis magna, congue quis, tempus eu, aliquam vitae, ante. Cras neque justo, ultrices at, rhoncus a, facilisis eget, nisl. Quisque vitae pede. Nam et augue. Sed a elit. Ut vel massa.</p>
                     <p>Suspendisse nibh pede, ultrices vitae, ultrices nec, mollis non, nibh. In sit amet pede quis leo vulputate hendrerit. Cras laoreet leo et justo auctor condimentum. Integer id enim. Suspendisse egestas, dui ac egestas mollis, libero orci hendrerit lacus, et malesuada lorem neque ac libero. Morbi tempor pulvinar pede. Donec vel elit. <a href="/about">далее</a></p>""").save()
    Page(slug='home_delivery', title=u'Оплата и доставка на главной', content=u'Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый владКаждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый вла').save()
    Page(slug='home_catalog', title=u'Ассортимент на главной', content=u'Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый владКаждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый вла').save()
    Page(slug='home_warranty', title=u'Гарантии на главной', content=u'Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый владКаждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый вла').save()
    Page(slug='home_sale', title=u'Акции и скидки на главной', content=u'Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый владКаждый влад Приветствуем вас в интернет-магазине автозапчастей. Каждый вла').save()
    
    Page(slug='about', title=u'О компании', content=u'Здесть пока ничего нет.').save()
    Page(slug='contacts', title=u'Контакты', content=u'Здесть пока ничего нет.').save()
    Page(slug='delivery', title=u'Доставка и оплата', content=u'Здесть пока ничего нет.').save()
    Page(slug='sale', title=u'Скидки и акции', content=u'Здесть пока ничего нет.').save()
    Page(slug='articles', title=u'Статьи', content=u'Здесть пока ничего нет.').save()
    Page(slug='warranty', title=u'Гарантии', content=u'Здесть пока ничего нет.').save()
    
def go_news():
    NewsItem.objects.all().delete()

    NewsItem(name=u'Навигаторы от prolodgy', text=u"""Integer velit. Vestibulum nisi nunc, accumsan ut, vehicula sit amet, porta a, mi. Nam nisl tellus, placerat eget, posuere eget, egestas eget, dui. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In elementum urna a eros. Integer iaculis. Maecenas vel elit.""").save()
    NewsItem(name=u'Навигаторы от prolodgy', text=u"""Integer velit. Vestibulum nisi nunc, accumsan ut, vehicula sit amet, porta a, mi. Nam nisl tellus, placerat eget, posuere eget, egestas eget, dui. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In elementum urna a eros. Integer iaculis. Maecenas vel elit.""").save()
    NewsItem(name=u'Навигаторы от prolodgy', text=u"""Integer velit. Vestibulum nisi nunc, accumsan ut, vehicula sit amet, porta a, mi. Nam nisl tellus, placerat eget, posuere eget, egestas eget, dui. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In elementum urna a eros. Integer iaculis. Maecenas vel elit.""").save()
