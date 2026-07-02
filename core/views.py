from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from core.models import Product

class IndexView(TemplateView):
    template_name = 'index.html'


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

# Como importar uma class para usar em apenas um template se não temos como trocar a rota no URL