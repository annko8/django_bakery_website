from django.shortcuts import render, get_list_or_404

from products.models import Categories, Products


def menu(request, category_slug):

    if category_slug == "all":
        products = Products.objects.all()
    else:
        products = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )

    categories = Categories.objects.all()

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
