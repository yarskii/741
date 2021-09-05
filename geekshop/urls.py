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
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff'), name='admin_staff'),
    path('', include('social_django.urls', namespace='social')),
    path('order/', include('ordersapp.urls', namespace='order')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
