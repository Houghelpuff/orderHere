from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'canes'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('order-here/', views.order_page, name='order_page'),
    path('thanks/', views.complete, name='thanks'),
    path('<int:id>/delete/', views.delete_order, name='delete'),
    path('<int:id>/details', views.get_details, name='details'),
]
