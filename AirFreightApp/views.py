import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
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


def air_upload_file(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        df = pd.read_excel(request.FILES.get('document'))
        df['BriefStatus'] = df['Status']
        df['BriefStatus'].replace(['Shipment delivered to consignee', 'Shipment departed from airport of origin',
                                   'Shipment handed over to another forwarder', 'Customs clearance completed',
                                   'Rejected declaration (by customs)', 'Consignee is a self-collector',
                                   'Shipment arrived at import gateway', 'Confirmation of exit received',
                                   'Shipment handed over to destination forwarder', 'Departure is checked',
                                   'Shipment booked on flight:', 'Shipment picked up',
                                   'Arrival Notice provided to customer/notify',
                                   'Customer order received and file opened',
                                   'Shipment discrepancy - consignee or agent has been informed of arrival',
                                   'Shipment arrived at airport of destination',
                                   'Shipment departed from export gateway',
                                   'Booking changed - order changed by principal',
                                   '(X)FWB received by carrier', 'Shipment delayed - flight departure delayed',
                                   'Arrival at exit', 'Shipment prepared for loading by carrier',
                                   'Shipment arrived at departure carrier', 'Shipment arrived at transit airport'],
                                  ['Delivered', 'Departed', 'Arranged', 'In Transit', 'Rejected', 'Self-Collection',
                                   'Arrived', 'In Transit', 'In Transit', 'Departed', 'In Transit', 'Collected',
                                   'Status Update To Customer', 'Delivered', 'Delayed', 'In Transit', 'Departed',
                                   'Booking Changed', 'Collected', 'Delayed', 'In Transit', 'In Transit', 'In Transit',
                                   'In Transit'], inplace=True)
        df['Shipmentdate'] = pd.to_datetime(df['Shipmentdate'], format='%d/%M/%Y').dt.strftime('%Y-%m-%d')
        df['ETD'] = pd.to_datetime(df['ETD'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
        df['ETA'] = pd.to_datetime(df['ETA'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

        df['Shipmentdate'] = df["Shipmentdate"].fillna("2000-01-01")
        df['ETD'] = df["ETD"].fillna("2000-01-01")
        df['ETA'] = df["ETA"].fillna("2000-01-01")
        for index, row in df.iterrows():
            air_shipment = AirFreightShipment()

            air_shipment.MasterOrder = row["Masterorder/Reference"]
            air_shipment.ShipmentNr = row["Shipmentno"]
            air_shipment.RPShipmentNr = row["RP Shipmentno"]
            air_shipment.SenderName = row["Sender Name"]
            air_shipment.ReceiverName = row["Receiver Name"]
            air_shipment.Country = row["Country"]
            air_shipment.City = row["City"]
            air_shipment.ZipCode = row["Zip Code"]
            air_shipment.CosigneeReference = row["Consignee Reference"]
            air_shipment.OrderNrCosignee = row["Order no. Consignor"]
            air_shipment.ShipmentInfo = row['Shipment Info']
            air_shipment.ShipmentDate = row["Shipmentdate"]
            air_shipment.ETD = row["ETD"]
            air_shipment.ETA = row["ETA"]
            air_shipment.Status = row["Status"]
            air_shipment.BriefStatus = row["BriefStatus"]

            air_shipment.save()

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file)
    return render(request, 'GroundShippingTemplates/upload.html', context)


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
