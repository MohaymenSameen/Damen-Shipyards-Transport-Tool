from django.contrib import admin
from django.urls import path
from DamenShipyardsApp.views import index_home_view
from OceanFreightApp.views import shipment_detail_view
from OceanFreightApp.views import index_dashboard_view
from AirFreightApp.views import air_freight_dashboard_view
from GroundShippingApp.views import ground_shipping_dashboard_view
urlpatterns = [
    path('', index_home_view, name='home'),
    path('dashboard/ocean', index_dashboard_view, name='ocean_dashboard'),
    path('OceanFreightApp', shipment_detail_view, name='OceanFreightApp'),
    path('dashboard/air', air_freight_dashboard_view, name='air_dashboard'),
    path('dashboard/ground', ground_shipping_dashboard_view, name='ground_dashboard'),
    path('admin/', admin.site.urls)
]
