from django.contrib import admin
from .models import Product, Brand, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "brand",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
