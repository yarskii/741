from django.urls import path

from .views import basket, basket_add, basket_remove, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>)/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket_edit, name='edit')
]
