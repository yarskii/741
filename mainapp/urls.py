# from django.contrib import admin
from django.urls import path
from .views import index

app_name = 'mainapp'

urlpatterns = [
    path('', index, name='index'),
    # path('<int:links_menu>/', index, name='category'),
]
