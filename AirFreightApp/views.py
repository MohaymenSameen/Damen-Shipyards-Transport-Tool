from django.shortcuts import render


# Create your views here.
def air_freight_dashboard_view(request, *args, **kwargs):
    return render(request, "AirFreightTemplates/air_freight_dashboard.html")
