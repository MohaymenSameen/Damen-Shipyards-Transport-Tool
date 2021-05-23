from django.shortcuts import render

from .models import OceanFreightShipment
from .resources import ShipmentResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


# Create your views here.
def shipment_detail_view(request):
    queryset = OceanFreightShipment.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, "OceanFreightTemplates/ocean_freight_shipment_detail.html", context)


def index_dashboard_view(request, *args, **kwargs):
    return render(request, "OceanFreightTemplates/ocean_freight_dashboard.html")




