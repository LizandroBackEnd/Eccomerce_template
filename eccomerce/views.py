from rest_framework import generics 
from .models import Category, Product 
from .serializers import CategorySerializer, ProductSerializer 
 
class CategoryList(generics.ListCreateAPIView): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 
     
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 
     
class ProductList(generics.ListCreateAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
     
class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer