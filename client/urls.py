from django.urls import path, include

from client.views import ClientListView, ClientCreateView, ClientDeleteView, ClientUpdateView

app_name = 'client'

urlpatterns = [
    path('', ClientListView.as_view(), name="client"),
    path('create/', ClientCreateView.as_view(), name="create"),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name="delete"),
] 