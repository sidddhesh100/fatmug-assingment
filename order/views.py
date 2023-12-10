import time
from datetime import datetime

from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Avg, Sum, ExpressionWrapper

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT

from .serializer import  OrderSerializer, CreateOrderSerializer
from .models import OrderModel
from vendor.models import VendorModel
# Create your views here.
class OrderView(APIView):
    def post(self, request, *args, **kwargs):
        """
        create order
        """        
        serializer = OrderSerializer(data=request.data)
        # import pdb
        # pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={
                    "status": True,
                    "message": "Order created",
                    "user": serializer.data
                }
            )
        return Response(
            status=HTTP_400_BAD_REQUEST,
            content_type="application/json",
            data={
                "status": False,
                "message": "Invalid user details",
                "allErrorMessage": serializer.errors
            }
        )
        
    def get(self, request, *args, **kwargs):
        """
        Get all the list of vendors
        """
        vendor_id = kwargs.get("vendor_id", None)
        data = OrderModel.objects.all()
        if vendor_id:
            data.filter(vendor=vendor_id)
        
        if len(data)>0:
            serializer = OrderSerializer(data, many=True)
            return Response(status=HTTP_200_OK,content_type="application/json", data={
                "status": True,
                "message": "Orders found successfully",
                "data": serializer.data
            })
        return Response(status=HTTP_404_NOT_FOUND,content_type="application/json", data={
                "status": False,
                "message": "Vendors not found"
            }) 
        
class OrderDetailsView(APIView):
    def get_object(self, po_id):
        try:
            return OrderModel.objects.get(po_number=po_id)
        except ObjectDoesNotExist:
            raise Http404
        
        
    def get(self, request, po_id, *args, **kwargs):
        """
        Get specific vendor by its po_id
        """
        order = self.get_object(po_id = po_id)
        serializer = OrderSerializer(order)
        return Response(status=HTTP_200_OK, content_type="application/json", data={"status": True, "message":"Vendor details found", "data": serializer.data})
    
    def delete(self, request, po_id, *args, **kwargs):
        """
        Delete vendor related to that po_id
        """
        vendor = self.get_object(po_id)
        vendor.delete()
        return Response(status=HTTP_204_NO_CONTENT, content_type="application/json", data={
            "status": True,
            "message": "Order deteled successfully"
        })
    
    def put(self, request, po_id, *args, **kwargs):
        """
        Update order respected to the po id
        """
        order = self.get_object(po_id)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={
                    "status": True,
                    "message": "Order Updated",
                    "order": serializer.data
                }
            )
        return Response(
            status=HTTP_400_BAD_REQUEST,
            content_type="application/json",
            data={
                "status": False,
                "message": "Invalid order update detials",
                "allErrorMessage": serializer.errors
            }
        )

class AcknowledgeOrderView(APIView):
    def post(self, request, po_id, *args, **kwargs):
        vendor_id = request.query_params.get("vendor_id", "")
        vendor = VendorModel.objects.filter(vendor_code=vendor_id)
        if not vendor.exists():
            return Response(
                status=HTTP_400_BAD_REQUEST,
                content_type="application/json",
                data={
                    "status": False,
                    "message": "vendor not exist"
                }
            )
        try:
            order = OrderModel.objects.get(po_number=po_id)
        except ObjectDoesNotExist:
            return Response(
                status=HTTP_404_NOT_FOUND,
                content_type="applicatoin/json",
                data={
                    "status": False,
                    "message": f"Order details not found for this po_id {po_id}"
                }
            )
        if order.vendor == vendor.first():
            
            order.acknowledgment_date = datetime.now()
            order.save()
            # all_orders = OrderModel.objects.get(vendor=order.vendor)
            # total_count = all_orders.count()
            # average_response_time = all_orders.filter(issue_date__isnull=False,acknowledgment_date__isnull=False).annotate(response_time=ExpressionWrapper(F('issue_date') - F('acknowledgment_date'),output_field=DurationField())).aggregate(avg_response_time=Sum('response_time'))
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={
                    "status": True,
                    "message": "Order acheknowledged"
                }
            )
        return Response(tatus=HTTP_400_BAD_REQUEST,
                content_type="application/json",
                data={
                    "status": False,
                    "message": f"{po_id} this order id not belongs to this vendor {vendor_id}"
                }
            )