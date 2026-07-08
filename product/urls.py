from django.urls import path, include

from product.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name="product"),
    path('create/', ProductCreateView.as_view(), name="create"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name="delete"),
] 