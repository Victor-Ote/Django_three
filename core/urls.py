from django.urls import path
from .views import IndexView, ProductListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('', ProductListView.as_view(), name='product'),
]