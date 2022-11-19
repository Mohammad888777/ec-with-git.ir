from django.db import models


class Category(models.Model):

    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return self.name

