from django.urls import path, include

from product.views import ProductListView, ProductCreateView

app_name = 'product'

urlpatterns = [
    path("", ProductListView.as_view(), name="product"),
    path("create/", ProductCreateView.as_view(), name="create")
] 