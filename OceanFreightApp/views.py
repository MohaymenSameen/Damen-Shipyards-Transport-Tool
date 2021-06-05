from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .ocean_table import OceanTable
from .models import OceanFreightShipment
from .ocean_shipment_filter import OceanShipmentFilter


class OceanListView(SingleTableMixin, FilterView):
    model = OceanFreightShipment
    table_class = OceanTable
    template_name = 'OceanFreightTemplates/ocean_freight_dashboard.html'
    filterset_class = OceanShipmentFilter
