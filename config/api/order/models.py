from django.db import models
from api.accounts.models import User
from api.product.models import Product


class Order(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=200)
    total_products=models.CharField(max_length=200,default=0)
    transaction_id=models.CharField(max_length=200,default=0)
    total_amount=models.CharField(max_length=200,default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.product_name

