from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import GroundShipment
from .resources import ShipmentResource


# Register your models here.

class GroundShippingAdmin(ImportExportModelAdmin):
    list_display = ('OrderNr',
                    'Status',
                    'TrackingNr',
                    'Contents',
                    'Weight',
                    'Dimensions',
                    'CollectionCompany',
                    'CollectionName',
                    'CollectionAddress',
                    'CollectionZipCode',
                    'CollectionCity',
                    'DeliveryCompany',
                    'DeliveryName',
                    'DeliveryAddress1',
                    'DeliveryAddress2',
                    'DeliveryZipCode',
                    'DeliveryCity',
                    'DeliveryCountryCode',
                    'Courier',
                    'CosigneeNr',
                    'ETC',
                    'ETA')
    resource_class = ShipmentResource


admin.site.register(GroundShipment, GroundShippingAdmin)
