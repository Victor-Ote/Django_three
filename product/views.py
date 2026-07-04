from django.shortcuts import render
from core.models import Product

from django.views.generic import TemplateView, ListView

class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'list.html'

    def dispatch(self, request, *args, **kwargs):

        print('Caiu para o App Product e está na view')

        return super().dispatch(request, *args, **kwargs) 