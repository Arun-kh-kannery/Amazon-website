from django.db import models
from django.contrib.auth.models import User
from shop.models  import Product
# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateField(auto_now_add=True)

    def subtotal(self):
        return  self.quantity*self.product.price

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items=models.IntegerField()
    address=models.TextField(max_length=200)
    phone=models.CharField(max_length=12)
    order_status=models.CharField(max_length=20,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")
    date_added=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def sub_total(self):
        return self.product.price*self.no_of_items




class Account(models.Model):
    acctnumber=models.IntegerField()
    acctype=models.CharField(max_length=50)
    balance=models.IntegerField()

    def __str__(self):
        # return '%s'%( self.acctnumber)
        return '{0}'.format(self.acctnumber)

