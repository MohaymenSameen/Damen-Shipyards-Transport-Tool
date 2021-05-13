from import_export import resources
from .models import AirFreightShipment


class ShipmentResource(resources.ModelResource):
    class meta:
        model = AirFreightShipment
