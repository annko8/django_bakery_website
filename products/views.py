from django.shortcuts import render

from products.models import Categories


def menu(request):

    categories = Categories.objects.all()

    context = {
        "title": "Menu",
        "products": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "Чайный столик и три стула",
                "description": "Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.",
                "price": 150.00,
            },
        ],
        "categories": categories,
    }
    return render(request, "products/menu.html", context)


def product(request):
    return render(request, "products/product.html")
