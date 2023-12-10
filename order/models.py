from django.db import models
from django.dispatch import receiver
from vendor.models import PerformanceModel
from django.db.models.signals import post_save
from django.db.models import F, Avg, ExpressionWrapper, fields
from django.db.models.functions import Coalesce


from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from vendor.models import VendorModel
# Create your models here.
class OrderModel(models.Model):
    PO_STATUS = (
        ("Pending", "Pending"),
        ("Complete", "Complete"),
        ("Cancelled", "Cancelled"),
    )
    po_number = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(VendorModel, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(choices=PO_STATUS, max_length=9, default="Pending")
    quality_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    issue_date = models.DateTimeField(null=True)
    acknowledgment_date = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "order" 
        
@receiver(post_save, sender=OrderModel)
def _post_save_receiver(sender, instance,**kwargs):
    vendor_orders = OrderModel.objects.filter(vendor=instance.vendor)
    completed_orders = vendor_orders.filter(status="Complete")

    count_delivered_on_time = vendor_orders.filter(issue_date__lte=F("delivery_date"), status="Complete").count()

    performance = PerformanceModel(vendor=instance.vendor, created_date=datetime.now())

    if instance.status == "Complete":
        total_completed_count = completed_orders.count()
        performance.on_time_delivery_rate = round((count_delivered_on_time / total_completed_count) * 10, 2)
        performance.quality_rating_avg = completed_orders.aggregate(avg_quality_rating=Avg("quality_rating"))["avg_quality_rating"]

    if instance.acknowledgment_date is not None:
        response_times = vendor_orders.filter(acknowledgment_date__isnull=False).annotate(
            subtraction_result=ExpressionWrapper(
                F('acknowledgment_date') - F('issue_date'),
                output_field=fields.FloatField()
            )
        ).aggregate(avg_subtraction=Coalesce(Avg('subtraction_result'), 0.0))

        performance.average_response_time = response_times["avg_subtraction"]

    total_orders = vendor_orders.count()
    performance.fulfillment_rate = round((count_delivered_on_time / total_orders) * 10, 2)

    performance.save()
    

