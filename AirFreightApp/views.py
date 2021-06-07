from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AirFreightShipment
from .air_table import AirTable
from .air_shipment_filter import AirShipmentFilter


class AirListView(SingleTableMixin, FilterView):
    model = AirFreightShipment
    table_class = AirTable
    template_name = "AirFreightTemplates/air_freight_dashboard.html"
    filterset_class = AirShipmentFilter

class AirChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):

        objects = AirFreightShipment.objects.all()

        # Dynamic shipment statuses
        newList = []
        newCount = []


        for shipment in objects:
            if shipment.BriefStatus not in newList:
                newList.append(shipment.BriefStatus)
                statuses = AirFreightShipment.objects.filter(BriefStatus=shipment.BriefStatus).count()
                newCount.append(statuses)

        data = {
            "labels": newList,
            "default": newCount
        }
        return Response(data)



