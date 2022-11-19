from .models import Order
from rest_framework import serializers


class OrderSerialzer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields=["user"]
        