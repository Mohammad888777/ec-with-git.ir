from django.db import models

from api.category.models import Category
from django.core.validators import FileExtensionValidator

class Product(models.Model):

    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200)
    stock=models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to="ProductIMG",null=True,blank=True,default="a.jpg",validators=[FileExtensionValidator(allowed_extensions=["jpg","jpeg","png"])])
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def  __str__(self) -> str:
        return self.name

