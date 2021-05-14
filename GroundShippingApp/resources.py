from import_export import resources
from .models import GroundShipment


class ShipmentResource(resources.ModelResource):
    class meta:
        model = GroundShipment
