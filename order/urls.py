from django.urls import path

from .views import AcknowledgeOrderView, OrderDetailsView, OrderView

urlpatterns = [
    path("", view=OrderView.as_view(), name="order"),
    path("<int:po_id>/", view=OrderDetailsView.as_view(), name="order_details"),
    path("<int:po_id>/acknowledge/", view=AcknowledgeOrderView.as_view(), name="order_details"),
]
