from django.shortcuts import render
from core.models import Product

from django.views.generic import TemplateView, ListView

class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = 'list.html'

    def dispatch(self, request, *args, **kwargs):

        print('Caiu para o App Product e está na view')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Produtos"
        context["total"] = Product.objects.count()

        return context