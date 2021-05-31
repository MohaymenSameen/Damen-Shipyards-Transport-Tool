from import_export import resources
from .models import AirFreightShipment


class ShipmentResource(resources.ModelResource):
    class Meta:
        model = AirFreightShipment
        import_id_fields = ('MasterOrder',)
        exclude = ('id',)
        skip_unchanged = True

    def skip_row(self, instance, original):
        if original.MasterOrder:
            return False
        return super(ShipmentResource, self).skip_row(instance, original)
