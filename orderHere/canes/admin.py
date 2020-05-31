from django.contrib import admin
from .models import Order
from .models import OptionalItems
from django.db import models


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Order for:", {"fields": ["order_name"]}),
        ("Main Course:", {"fields": ["main_food"]})
    ]


class OptionalItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Additional Item to Display:", {"fields": ["item_name"]})
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OptionalItems, OptionalItemsAdmin)
