from django.urls import path, include
from django.contrib import admin
# import mainapp.views as mainapp
from geekshop.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('products/', include('mainapp.urls', namespace='products'), name='products'),
    path('contacts/', contacts, name='contacts'),
    path('admin/', admin.site.urls,),
]
