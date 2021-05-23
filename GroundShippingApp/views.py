from django.shortcuts import render


# Create your views here.
def ground_shipping_dashboard_view(request, *args, **kwargs):
    return render(request, "GroundShippingTemplates/ground_shipping_dashboard.html")
