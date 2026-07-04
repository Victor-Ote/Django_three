from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# from core.models import Product

class IndexView(TemplateView):
    template_name = 'index.html'
