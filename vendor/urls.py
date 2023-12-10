from django.contrib import admin
from django.urls import path
from .views import CreateVendorView, VendorView, VendorPerformanceView

urlpatterns = [
    path('', view=CreateVendorView.as_view(), name="create_vendor"),
    path('<int:vendor_id>/', view=VendorView.as_view(), name="vendor"),
    path('<int:vendor_id>/performance/', view=VendorPerformanceView.as_view(), name="vendor_performcne"),
]
