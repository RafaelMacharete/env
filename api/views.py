from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def listarProdutos(request):
    if request.method == "GET":
        queryset = Produto.objects.all() # seleciona todos os produtos
        serializer = ProdutoSerializer(queryset, many=True) # transforma em JSON
        return Response(serializer.data)
    elif request.method == 'POST': 
        serializer = ProdutoSerializer(data = request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)