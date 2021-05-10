from import_export import resources
from .models import Shipment


class ShipmentResource(resources.ModelResource):
    class meta:
        model = Shipment
