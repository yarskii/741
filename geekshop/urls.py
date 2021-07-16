from django.urls import path, include
from django.contrib import admin
import mainapp.views as mainapp
from geekshop.views import index, contacts

urlpatterns = [
    path('', index),
    path('products/', include('mainapp.urls')),
    path('contacts/', contacts),
    path('admin/', admin.site.urls),
]
