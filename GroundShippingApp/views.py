from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .models import GroundShipment
from .ground_table import GroundTable
from .ground_shipment_filter import GroundShipmentFilter
from rest_framework.views import APIView
from rest_framework.response import Response


class GroundListView(SingleTableMixin, FilterView):
    model = GroundShipment
    table_class = GroundTable
    template_name = "GroundShippingTemplates/ground_shipping_dashboard.html"
    filterset_class = GroundShipmentFilter


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):

        objects = GroundShipment.objects.all()

        # Dynamic shipment statuses
        newList = []
        newCount = []
        for shipment in objects:
            if shipment.Status not in newList:
                newList.append(shipment.Status)
                statuses = GroundShipment.objects.filter(Status=shipment.Status).count()
                newCount.append(statuses)

        data = {
            "labels": newList,
            "default": newCount
        }
        return Response(data)
