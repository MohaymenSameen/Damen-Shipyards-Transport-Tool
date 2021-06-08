import pandas as pd
from django.shortcuts import render
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from rest_framework.views import APIView
from rest_framework.response import Response
from .ocean_table import OceanTable
from .models import OceanFreightShipment
from .ocean_shipment_filter import OceanShipmentFilter
from django.core.files.storage import FileSystemStorage


class OceanListView(SingleTableMixin, FilterView):
    model = OceanFreightShipment
    table_class = OceanTable
    template_name = 'OceanFreightTemplates/ocean_freight_dashboard.html'
    filterset_class = OceanShipmentFilter


def upload_file(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        df = pd.read_excel(request.FILES.get('document'))

        df['ETD Date (GMT Time)'] = pd.to_datetime(df['ETD Date (GMT Time)'], format='%d/%M/%Y %H%M').dt.strftime(
            '%Y-%m-%d %H:%M')
        df['ETA Date (GMT Time)'] = pd.to_datetime(df['ETA Date (GMT Time)'], format='%d/%M/%Y %H%M',
                                                   errors='coerce').dt.strftime('%Y-%m-%d %H:%M')
        df['CTA Date (GMT Time)'] = pd.to_datetime(df['CTA Date (GMT Time)'], format='%d/%M/%Y %H%M',
                                                   errors='coerce').dt.strftime('%Y-%m-%d %H:%M')
        df["MainShipmentId"] = df["STT"].astype(str) + df["Container No"].astype(str)
        df["MainShipmentId"] = df["MainShipmentId"].str.replace(' ', '')

        df['ETD Date (GMT Time)'] = df["ETD Date (GMT Time)"].fillna("2000-01-01")
        df['ETA Date (GMT Time)'] = df["ETA Date (GMT Time)"].fillna("2000-01-01")
        df['CTA Date (GMT Time)'] = df["CTA Date (GMT Time)"].fillna("2000-01-01")

        df["STT"] = df["STT"].fillna("")
        df["Container Weight"] = df["Container Weight"].fillna(0)
        df["Container Volume"] = df["Container Volume"].fillna(0.0)

        for index, row in df.iterrows():
            ocean_freight_shipment = OceanFreightShipment()

            ocean_freight_shipment.MainShipmentId = row["MainShipmentId"]
            ocean_freight_shipment.ShipmentId = pd.to_numeric(row["STT"])
            ocean_freight_shipment.ContainerNr = row["Container No"]
            ocean_freight_shipment.Departure = row["Departure Port"]
            ocean_freight_shipment.Destination = row["Destination Port"]
            ocean_freight_shipment.ScheduledDeparture = row["ETD Date (GMT Time)"]
            ocean_freight_shipment.ScheduledArrival = row["ETA Date (GMT Time)"]
            ocean_freight_shipment.RevisedArrival = row["CTA Date (GMT Time)"]
            ocean_freight_shipment.TotalVolume = pd.to_numeric(row["Container Volume"])
            ocean_freight_shipment.TotalWeight = pd.to_numeric(row["Container Weight"])
            ocean_freight_shipment.Dimensions = row['Container Movement']
            ocean_freight_shipment.Carrier = row["Carrier"]
            ocean_freight_shipment.ShipperReference = row["Shipper Reference"]

            ocean_freight_shipment.save()

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file)
    return render(request, 'OceanFreightTemplates/upload.html', context)


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
