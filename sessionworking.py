# -*- coding: utf-8 -*-

from catalog.models import Item

class SessionCartWorking(object):
    def __init__(self, request):
        self.__request = request
        
    def var(self, item):
        return 'cart_' + str(item)
        
    def add_to_cart(self, cap, item):
        self.__request.session[self.var(item)] = 1
    
    def del_from_cart(self, cap, item):
        del self.__request.session[self.var(item)]

    def get_content(self, cap):
        res = []
        for i in self.__request.session.keys():
            if i.startswith('cart_'):
                res.append({'item': Item.get(int(i[5:])),
                     'count': int(self.__request.session[i])})
        return res
    
    def pop_content(self):
        res = []
        for i in self.__request.session.keys():
            if i.startswith('cart_'):
                res.append({'item': Item.get(int(i[5:])),
                     'count': int(self.__request.session[i])})
                del self.__request.session[i]
        return res
    
    def get_goods_count_and_sum(self, cap):
        cart = self.get_content(cap)
        return (sum([x['count'] for x in cart]), sum([x['count'] * x['item'].price for x in cart]))
    
    def count_plus(self, cap, item):
        self.__request.session[self.var(item)] += 1
        
    def count_minus(self, cap, item):
        if self.__request.session[self.var(item)] <= 1:
            self.del_from_cart(cap, item)
        else:
            self.__request.session[self.var(item)] -= 1
    
    