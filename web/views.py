from django.shortcuts import render
from django.views import View
from .models import ProductModel


class ProductView(View):
    def get(self, request):
        products = ProductModel.objects.all()
        return render(request, 'product.html', {"products": products})
