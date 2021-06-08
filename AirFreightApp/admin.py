from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AirFreightShipment
from .resources import ShipmentResource


# Register your models here.

class AirFreightAdmin(ImportExportModelAdmin):
    list_display = ('MasterOrder',
                    'ShipmentNr',
                    'RPShipmentNr',
                    'SenderName',
                    'ReceiverName',
                    'Country',
                    'City',
                    'ZipCode',
                    'CosigneeReference',
                    'OrderNrCosignee',
                    'ShipmentInfo',
                    'ShipmentDate',
                    'ETD',
                    'ETA',
                    'Status',
                    'BriefStatus')
    resource_class = ShipmentResource


admin.site.register(AirFreightShipment, AirFreightAdmin)
