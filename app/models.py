from django.db import models

# Create your models here.

class CartOrder(models.Model):
    customer = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    payment = models.CharField(max_length=50)  # Store payment method name
    items = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}"
        

