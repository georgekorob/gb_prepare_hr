from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product

# app_name = 'djapp'


# Create your views here.
class ProductView(ListView):
    model = Product
    template_name = 'djapp/goods_list.html'
    queryset = Product.objects.all()
