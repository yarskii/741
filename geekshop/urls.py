from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from geekshop.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('contacts/', contacts, name='contacts'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
