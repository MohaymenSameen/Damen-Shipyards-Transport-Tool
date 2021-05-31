import django_tables2 as tables
from .models import AirFreightShipment


class AirTable(tables.Table):
    class Meta:
        model = AirFreightShipment
        template_name = "django_tables2/bootstrap4.html"
