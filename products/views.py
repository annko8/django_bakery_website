from django.shortcuts import render

from products.models import Categories, Products


def menu(request):

    categories = Categories.objects.all()
    products = Products.objects.all()

    context = {
        "title": "Menu",
        "products": products,
        "categories": categories,
    }
    return render(request, "products/menu.html", context)


def product(request):
    return render(request, "products/product.html")
