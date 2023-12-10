from rest_framework import serializers
from .models import OrderModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"
        
class CreateOrderSerializer(serializers.ModelSerializer):
    delivery_date = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = OrderModel
        fields = ["vendor", "delivery_date", "items", "quantity", "quality_rating"]