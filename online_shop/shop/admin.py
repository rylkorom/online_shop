from django.contrib import admin
from .models import *


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductImages)

