from django.shortcuts import render
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView

from client.models import Client


class ClientListView(ListView):
    model = Client
    context_object_name = "client"
    template_name = 'clientList.html'
    

    def dispatch(self, request, *args, **kwargs):
        print('Entrou ma View do client ', request.method)
        return super().dispatch(request, *args, **kwargs)
