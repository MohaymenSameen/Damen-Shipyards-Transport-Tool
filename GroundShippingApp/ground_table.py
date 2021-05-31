from django_tables2 import tables
from .models import GroundShipment


class GroundTable(tables.Table):
    class Meta:
        model = GroundShipment
        template_name = "django_tables2/bootstrap4.html"
