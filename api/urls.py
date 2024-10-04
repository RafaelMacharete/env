from django.urls import path
from .views import listarProdutos

urlpatterns = [
    path('listarProdutos', listarProdutos),
]
