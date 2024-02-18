from django.contrib import admin

from products.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class Productsdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
