from django.urls import path
from . import views 

urlpatterns = [
    path('listarProdutos', views.listarProdutos),
]

