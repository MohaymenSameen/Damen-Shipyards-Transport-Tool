from import_export import resources
from .models import OceanFreightShipment


class ShipmentResource(resources.ModelResource):
    class Meta:
        model = OceanFreightShipment
        import_id_fields = ('ShipmentId',)
        exclude = ('id',)
        skip_unchanged = True

    def skip_row(self, instance, original):
        if original.ShipmentId:
            return False
        return super(ShipmentResource, self).skip_row(instance, original)
