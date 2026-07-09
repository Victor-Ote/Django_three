from urllib import request

from django.shortcuts import render
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView

from client.models import Client


class ClientListView(ListView):
    model = Client
    context_object_name = "client"
    template_name = 'clientList.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Client.objects.count()
        context['title'] = 'Clientes'
        return context
    
class ClientCreateView(CreateView):
    model = Client
