import django_filters as filters
from .models import AirFreightShipment


class AirShipmentFilter(filters.FilterSet):
    class Meta:
        model = AirFreightShipment
        fields = ['MasterOrder', 'CosigneeReference']