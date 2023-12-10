from rest_framework.serializers import ModelSerializer
from .models import VendorModel, PerformanceModel
import time

class CreateVendorSerializer(ModelSerializer):
    class Meta(object):
        model = VendorModel
        fields = ["name", "contact_details", "address"]
        
        
        
class VendorSerializer(ModelSerializer):
    class Meta(object):
        model = VendorModel
        fields = "__all__"
        
class PerformanceSerializer(ModelSerializer):
    class Meta(object):
        model=PerformanceModel
        fields="__all__"