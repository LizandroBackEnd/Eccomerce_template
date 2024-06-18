from rest_framework import generics 
from .models import Category, Product 
from .serializers import CategorySerializer, ProductSerializer 
from rest_framework.permissions import IsAuthenticated 
 
class CategoryList(generics.ListCreateAPIView): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer  
    permission_classes = [IsAuthenticated]
     
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer  
    permission_classes = [IsAuthenticated]
     
class ProductList(generics.ListCreateAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [IsAuthenticated] 
     
class ProductDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [IsAuthenticated]