from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer

class LatestProductsLists(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4] # first 4 products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)