from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .models import GroundShipment
from .ground_table import GroundTable
from .ground_shipment_filter import GroundShipmentFilter
class GroundListView(SingleTableMixin, FilterView):
    model = GroundShipment
    table_class = GroundTable
    template_name = "GroundShippingTemplates/ground_shipping_dashboard.html"
    filterset_class = GroundShipmentFilter

