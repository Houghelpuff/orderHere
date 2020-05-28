from django.db import models

FOOD = [('3 Piece', '3 Piece'), ('Box Combo', 'Box Combo'),
        ('Caniac Combo', 'Caniac Combo')]

DRINKS = [('Sweet Tea', 'Sweet Tea'), ('Unsweet Tea', 'Unsweet Tea'),
          ('Coke', 'Coke'), ('Dr. Pepper', 'Dr. Pepper')]


class Order(models.Model):
    order_name = models.CharField(max_length=50)
    main_food = models.CharField(
        max_length=20, choices=FOOD, default='Cane\'s order')
    drink = models.CharField(
        max_length=15, choices=DRINKS, default='Drink Choice')

    def __str__(self):
        return self.order_name
