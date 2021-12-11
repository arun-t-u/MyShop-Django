from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category', 'price', 'stock', 'is_avilable', 'modified_date')
    prepopulated_fields = {"slug" : ("product_name",)}

admin.site.register(Product, ProductAdmin)