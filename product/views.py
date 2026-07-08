from product.models import Product

from django.views.generic import  ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = 'list.html'

    def dispatch(self, request, *args, **kwargs):
        print('Fez o GET: ', request.method)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Produtos"
        context["total"] = Product.objects.count()
        return context
    
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product:product')
    template_name = 'create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('Fez o POST: ', self.request.method)
        context["title"] = "Criar Produto"
        return context
    
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('product:product')
    template_name = 'create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('Fez o Uptade: ', self.request.method)
        return context
    
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product')
