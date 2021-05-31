from import_export import resources
from .models import GroundShipment


class ShipmentResource(resources.ModelResource):
    class Meta:
        model = GroundShipment
        import_id_fields = ('OrderNr',)
        exclude = ('id',)
        skip_unchanged = True

    def skip_row(self, instance, original):
        if original.OrderNr:
            return False
        return super(ShipmentResource, self).skip_row(instance, original)
