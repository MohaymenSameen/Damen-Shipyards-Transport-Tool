from django.shortcuts import render

from .models import Shipment
# Create your views here.
def shipment_detail_view(request):
    queryset = Shipment.objects.all()

    context = {
        'object_list': queryset
    }
    return render(request, "shipments/shipment_detail.html", context)