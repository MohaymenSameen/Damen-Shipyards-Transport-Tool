import django_filters as filters
from .models import OceanFreightShipment


class OceanShipmentFilter(filters.FilterSet):
    class Meta:
        model = OceanFreightShipment
        fields = ['ShipmentId', 'ShipperReference']
