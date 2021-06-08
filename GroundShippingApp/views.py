import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
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


def ground_upload_file(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        df = pd.read_excel(request.FILES.get('document'))
        df['Dimensions'] = df['Length'].map(str) + 'L-' + df['Width'].map(str) + 'W-' + df['Height'].map(str) + 'H'
        df['ETC'] = df["ETC"].fillna("2000-01-01")
        df['ETA'] = df["ETA"].fillna("2000-01-01")

        for index, row in df.iterrows():
            ground_shipment = GroundShipment()

            ground_shipment.OrderNr = row["Order No."]
            ground_shipment.Status = row["Status"]
            ground_shipment.TrackingNr = row["Tracking No."]
            ground_shipment.Contents = row["Contents"]
            ground_shipment.Weight = row["Weight"]
            ground_shipment.Dimensions = row["Dimensions"]
            ground_shipment.CollectionCompany = row["Collection Address Company Name"]
            ground_shipment.CollectionName = row["Collection Address Name"]
            ground_shipment.CollectionAddress = row["Collection Address Address"]
            ground_shipment.CollectionZipCode = row["Collection Address Postal Code/ZIP"]
            ground_shipment.CollectionCity = row['Collection Address City']
            ground_shipment.DeliveryCompany = row["Delivery Address Company Name"]
            ground_shipment.DeliveryName = row["Delivery Address Name"]
            ground_shipment.DeliveryAddress1 = row["Delivery Address Address"]
            ground_shipment.DeliveryAddress2 = row["Delivery Address Address Line 2"]
            ground_shipment.DeliveryZipCode = row["Delivery Address Postal Code/ZIP"]
            ground_shipment.DeliveryCity = row["Delivery Address City"]
            ground_shipment.DeliveryCountryCode = row["Delivery Address Country"]
            ground_shipment.Reference = row["Reference"]
            ground_shipment.Courier = row["Consignment No."]
            ground_shipment.CosigneeNr = row["Courier"]
            ground_shipment.ETC = row["ETC"]
            ground_shipment.ETA = row["ETA"]

            ground_shipment.save()

        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file)
    return render(request, 'GroundShippingTemplates/upload.html', context)


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
