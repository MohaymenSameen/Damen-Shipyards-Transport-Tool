from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import OceanFreightShipment
from .resources import ShipmentResource


class OceanFreightAdmin(ImportExportModelAdmin):
    list_display = ('MainShipmentId',
                    'ShipmentId',
                    'ContainerNr',
                    'Departure',
                    'Destination',
                    'ScheduledDeparture',
                    'ScheduledArrival',
                    'RevisedArrival',
                    'TotalVolume',
                    'TotalWeight',
                    'Dimensions',
                    'Carrier',
                    'ShipperReference')
    resource_class = ShipmentResource


admin.site.register(OceanFreightShipment, OceanFreightAdmin)
