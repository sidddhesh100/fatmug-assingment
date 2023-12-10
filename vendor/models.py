from django.core.validators import (
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models


# Create your models here.
class VendorModel(models.Model):
    name = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    contact_details = models.CharField(validators=[MinLengthValidator(10)], max_length=10)
    address = models.CharField(validators=[MinLengthValidator(15)], max_length=50)
    # vendor_code = models.CharField(validators=[MinLengthValidator(12)], max_length=12, unique=True, primary_key=True)
    vendor_code = models.AutoField(primary_key=True)

    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    average_response_time = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)

    class Meta:
        db_table = "vendor"


class PerformanceModel(models.Model):
    vendor = models.OneToOneField(VendorModel, on_delete=models.DO_NOTHING, primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    quality_rating_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    average_response_time = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    fulfillment_rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)

    class Meta:
        db_table = "performance"
