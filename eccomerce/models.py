from django.db import models

# Create your models here. 
 
class Category(models.Model): 
    name = models.CharField(max_length=200) 
    description = models.TextField() 
     
    def __str__(self): 
        return self.name 
     
class Product(models.Model): 
    name = models.CharField(max_length=200) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.IntegerField() 
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) 

    def __str__(self): 
        return self.name 