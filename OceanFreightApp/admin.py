from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Shipment

admin.site.register(Shipment, ImportExportModelAdmin)


class ShipmentAdmin(ImportExportModelAdmin):
    list_display = ('ShipmentId',
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
