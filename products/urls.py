from django.urls import path
from products import views

app_name = "products"

urlpatterns = [
    path("", views.menu, name="menu"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
