from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory


# Create your views here.
class ProductView(ListView):
    model = Product
    template_name = 'djapp/goods_list.html'

    # queryset = Product.objects.prefetch_related('categories').all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super(ProductView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        if pk is None or pk == 0:
            cur_category = {'name': 'все'}
            context['products'] = Product.objects.prefetch_related('categories').all()
        else:
            cur_category = get_object_or_404(ProductCategory, pk=pk)
            context['products'] = Product.objects.filter(categories__in=[pk]).prefetch_related('categories').order_by(
                'price')
        context['category'] = cur_category
        return context
