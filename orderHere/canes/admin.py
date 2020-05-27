from django.contrib import admin
from .models import Order
from django.db import models


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order for:", {"fields": ["order_name"]}),
        ("Main Course:", {"fields": ["main_food"]})
    ]


admin.site.register(Order, OrderAdmin)
