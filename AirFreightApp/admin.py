from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AirFreightShipment

# Register your models here.
admin.site.register(AirFreightShipment, ImportExportModelAdmin)


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
                    'Status')
