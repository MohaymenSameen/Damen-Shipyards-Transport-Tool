from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from rest_framework.views import APIView
from rest_framework.response import Response
from .ocean_table import OceanTable
from .models import OceanFreightShipment
from .ocean_shipment_filter import OceanShipmentFilter


class OceanListView(SingleTableMixin, FilterView):
    model = OceanFreightShipment
    table_class = OceanTable
    template_name = 'OceanFreightTemplates/ocean_freight_dashboard.html'
    filterset_class = OceanShipmentFilter


class OceanChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        objects = OceanFreightShipment.objects.all().count()

        # Using lists as chart.js only uses lists instead of single variables
        newLabels = []
        newCount = []

        newLabels.append("Total Shipments")
        newCount.append(objects)

        data = {
            "labels": newLabels,
            "default": newCount
        }
        return Response(data)
