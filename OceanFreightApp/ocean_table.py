import django_tables2 as tables
from .models import OceanFreightShipment


class OceanTable(tables.Table):
    class Meta:
        model = OceanFreightShipment
        template_name = "django_tables2/bootstrap4.html"
