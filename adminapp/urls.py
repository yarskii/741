from adminapp.views import (
    UsersListView,
    UsersCreateView,
    user_update,
    user_delete,
    category_create,
    categories,
    ProductCategoryUpdateView,
    category_delete,
    product_create,
    ProductDetailView,
    product_update,
    product_delete,
    products
    )
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', UsersCreateView.as_view(), name='user_create'),
    path('users/read/', UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user_update, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),

    path('categories/create/', category_create, name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', category_delete, name='category_delete'),

    path('products/create/category/<int:pk>/', product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/<int:pk>/', ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]
