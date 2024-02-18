from django.shortcuts import render

from products.models import Categories, Products


def menu(request, category_slug):
    order_by = request.GET.get("order_by", None)

    if category_slug == "all":
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=category_slug)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    categories = Categories.objects.all()

    context = {
        "title": "Menu",
        "products": products,
        "categories": categories,
        "slug_url": category_slug,
    }
    return render(request, "products/menu.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }
    return render(request, "products/product.html", context=context)
