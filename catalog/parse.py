 # -*- coding: utf-8 -*-

import sys
import re
from django.conf import settings
from car_model import CarModel
from category import Category
from item import Colour, Item

def process(price_line):
    print price_line
    price_line = price_line.strip().split(',')
    category = price_line[0].decode('utf-8')
    name = price_line[1].decode('utf-8')
    art = price_line[2].decode('utf-8')
    cars = price_line[3].decode('utf-8').split(' ')
    colour = price_line[4].decode('utf-8')
    price = price_line[9].decode('utf-8')
    if price == '':
        price = 0
    profit = price_line[11].decode('utf-8')
    category = Category.add_and_get(category)
    colour = Colour.add_and_get(colour)
    for c in cars:
        car = CarModel.add_and_get(c)
        if car:
            Item(category=category,
                 car_model=car,
                 colour=colour,
                 name=name,
                 art=art,
                 price=price,
                 profit=profit).save()
        

def go(filename):
    file_from = open(filename, 'r')
    first = True
    for l in file_from:
        if not first:
            process(l)
        else:
            first = False
            