from django.db import models
from app import views

# Create your models here.
class CartOrder(models.Model):
    customer=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    payment=models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    items=models.CharField(max_length=100)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"
        

