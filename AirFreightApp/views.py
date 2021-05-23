from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .models import AirFreightShipment
from .air_table import AirTable
from .air_shipment_filter import AirShipmentFilter


class AirListView(SingleTableMixin, FilterView):
    model = AirFreightShipment
    table_class = AirTable
    template_name = "AirFreightTemplates/air_freight_dashboard.html"
    filterset_class = AirShipmentFilter



