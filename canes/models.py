from django.db import models
from django import forms
from multiselectfield import MultiSelectField
from django.db.models import Count

FOOD = [('3 Piece', '3 Piece'), ('Box Combo', 'Box Combo'),
        ('Caniac Combo', 'Caniac Combo')]

DRINKS = [('Sweet Tea', 'Sweet Tea'), ('Unsweet Tea', 'Unsweet Tea'),
          ('Coke', 'Coke'), ('Dr. Pepper', 'Dr. Pepper')]


class OptionalItems(models.Model):
    item_name = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name


class Order(models.Model):
    order_name = models.CharField(max_length=50)
    main_food = models.CharField(
        max_length=20, choices=FOOD, default='Cane\'s order')
    drink = models.CharField(
        max_length=15, choices=DRINKS, default='Drink Choice')
    additional_items = models.ManyToManyField(OptionalItems)
    additional_notes = models.TextField(default='More notes')

    def __str__(self):
        return self.order_name
