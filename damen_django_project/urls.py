from django.contrib import admin
from django.urls import path
from DamenShipyardsApp.views import index_home_view, login_view, logout_view
from OceanFreightApp.views import OceanListView
from AirFreightApp.views import AirListView, AirChartData
from GroundShippingApp.views import GroundListView, ChartData
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', index_home_view, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('dashboard/ocean', login_required(OceanListView.as_view())),
    path('dashboard/air', login_required(AirListView.as_view())),
    path('dashboard/ground', login_required(GroundListView.as_view())),
    path('dashboard/ground/api/chart/data', login_required(ChartData.as_view())),
    path('dashboard/air/api/chart/data', login_required(AirChartData.as_view())),
    path('admin/', admin.site.urls)
]
