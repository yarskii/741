from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def index(request):

    links_menu = ProductCategory.objects.all()
    #     [
    #     {'href': 'index', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    #     {'href': 'products_new', 'name': 'новинки'},
    # ]

    products = Product.objects.all()[:4]

    context = {
        'links_menu': links_menu,
        'related_products': products,
    }
    return render(request, 'mainapp/products.html', context)

