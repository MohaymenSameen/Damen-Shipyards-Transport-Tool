from django.shortcuts import render

from .models import Shipment
from .resources import ShipmentResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


# Create your views here.
def shipment_detail_view(request):
    queryset = Shipment.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, "SchenkerTemplates/schenker_shipment_detail.html", context)


def index_dashboard_view(request, *args, **kwargs):
    return render(request, "Dashboard/index.html")

def simple_upload(request):
    if request.method == 'POST':
        shipment_resource = ShipmentResource()
        dataset = Dataset()
        new_shipment = request.FILES['myFile']

        if not new_shipment.name.endswith('xlsx' or 'xls'):
            messages.info(request, 'wrong format')
            return render(request, 'SchenkerTemplates/schenker_shipment_detail.html')
        imported_data = dataset.load(new_shipment.read(), format='xlsx')
        for data in imported_data:
            value = Shipment(data[2], data[4], data[23], data[27], data[24], data[28], data[29], data[9], data[10],
                             data[13], data[11], data[21])
            value.save()
    return render(request, 'SchenkerTemplates/schenker_shipment_detail.html')


