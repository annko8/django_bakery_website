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


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }
    return render(request, "products/product.html", context=context)
