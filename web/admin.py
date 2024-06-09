from django.contrib import admin
from .models import ProductModel, Order, CategoryModel

admin.site.register(Order)
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
