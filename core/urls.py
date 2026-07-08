from django.urls import path, include
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("products/", include("product.urls")),
    path('clients/', include('client.urls')),
    # path('order', include('product.urls')),
]