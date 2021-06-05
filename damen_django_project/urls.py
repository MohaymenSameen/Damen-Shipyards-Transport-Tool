from django.contrib import admin
from django.urls import path
from DamenShipyardsApp.views import index_home_view
from OceanFreightApp.views import OceanListView
from AirFreightApp.views import AirListView
from GroundShippingApp.views import GroundListView, ChartData

urlpatterns = [
    path('', index_home_view, name='home'),
    path('dashboard/ocean', OceanListView.as_view()),
    path('dashboard/air', AirListView.as_view()),
    path('dashboard/ground', GroundListView.as_view()),
    path('dashboard/ground/api/chart/data', ChartData.as_view()),
    path('admin/', admin.site.urls)
]
