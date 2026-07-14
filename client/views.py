from urllib import request

from django.shortcuts import render
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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
    fields = '__all__'
    success_url = reverse_lazy('client:client')
    template_name = 'clientsCreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Criar Cliente'
        return context
    
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client')