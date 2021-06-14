from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.static import serve

from DamenShipyardsApp.views import index_home_view, login_view, logout_view
from OceanFreightApp.views import OceanListView, OceanChartData, upload_file
from AirFreightApp.views import AirListView, AirChartData, air_upload_file
from GroundShippingApp.views import GroundListView, ChartData, ground_upload_file
from django.contrib.auth.decorators import login_required

from damen_django_project import settings

urlpatterns = [
    path('', index_home_view, name='home'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('dashboard/ocean', login_required(OceanListView.as_view()), name='oceandashboard'),
    path('dashboard/ocean/upload', login_required(upload_file), name='uploadoceanfile'),
    path('dashboard/ground/upload', login_required(ground_upload_file), name='uploadgroundfile'),
    path('dashboard/air/upload', login_required(air_upload_file), name='uploadairfile'),
    path('dashboard/air', login_required(AirListView.as_view()), name='airdashboard'),
    path('dashboard/ground', login_required(GroundListView.as_view()), name='grounddashboard'),
    path('dashboard/ground/api/chart/data', login_required(ChartData.as_view())),
    path('dashboard/air/api/chart/data', login_required(AirChartData.as_view())),
    path('dashboard/ocean/api/chart/data', login_required(OceanChartData.as_view())),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATICFILES_DIRS}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
