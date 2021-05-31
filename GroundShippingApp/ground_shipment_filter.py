import django_filters as filters
from .models import GroundShipment


class GroundShipmentFilter(filters.FilterSet):
    class Meta:
        model = GroundShipment
        fields = ['OrderNr', 'CosigneeNr']
