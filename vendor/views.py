from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)
from rest_framework.views import APIView

from .models import PerformanceModel, VendorModel
from .serializer import CreateVendorSerializer, PerformanceSerializer, VendorSerializer


# Create your views here.
class CreateVendorView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        create vendor view
        """
        serializer = CreateVendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={"status": True, "message": "User created", "user": serializer.data},
            )
        return Response(
            status=HTTP_400_BAD_REQUEST,
            content_type="application/json",
            data={"status": False, "message": "Invalid user details", "allErrorMessage": serializer.errors},
        )

    def get(self, request, *args, **kwargs):
        """
        Get all the list of vendors
        """
        data = VendorModel.objects.all()
        if len(data) > 0:
            serializer = VendorSerializer(data, many=True)
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={"status": True, "message": "Vendors found successfully", "data": serializer.data},
            )
        return Response(
            status=HTTP_404_NOT_FOUND, content_type="application/json", data={"status": False, "message": "Vendors not found"}
        )


class VendorView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, vendor_id):
        try:
            return VendorModel.objects.get(vendor_code=vendor_id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, vendor_id, *args, **kwargs):
        """
        Get specific vendor by its vendor_id
        """
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor)
        return Response(
            status=HTTP_200_OK,
            content_type="application/json",
            data={"status": True, "message": "Vendor details found", "data": serializer.data},
        )

    def delete(self, request, vendor_id, *args, **kwargs):
        """
        Delete vendor related to that vendor_id
        """
        vendor = self.get_object(vendor_id)
        vendor.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
            content_type="application/json",
            data={"status": True, "message": "Vendor deteled successfully"},
        )

    def put(self, request, vendor_id, *args, **kwargs):
        """
        Update vendor respected to the vendor id
        """
        vendor = self.get_object(vendor_id)
        serializer = VendorSerializer(vendor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                status=HTTP_200_OK,
                content_type="application/json",
                data={"status": True, "message": "Vendor Updated", "vendor": serializer.data},
            )
        return Response(
            status=HTTP_400_BAD_REQUEST,
            content_type="application/json",
            data={"status": False, "message": "Invalid user details", "allErrorMessage": serializer.errors},
        )


class VendorPerformanceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, vendor_id, *args, **kwargs):
        try:
            performance = PerformanceModel.objects.get(vendor=vendor_id)
        except ObjectDoesNotExist:
            return Response(
                status=HTTP_404_NOT_FOUND,
                content_type="application/json",
                data={"status": False, "message": f"Performance report not found for this vendor_id {vendor_id}"},
            )
        serializer = PerformanceSerializer(performance)
        return Response(
            status=HTTP_200_OK,
            content_type="application/json",
            data={"status": True, "message": "Vendor Updated", "data": serializer.data},
        )
