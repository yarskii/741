# from django.contrib import admin
from django.urls import path
from .views import products

app_name = 'mainapp'

urlpatterns = [
    path('', products, name='products_index'),
    path('category/<int:pk>/', products, name='category'),
]
