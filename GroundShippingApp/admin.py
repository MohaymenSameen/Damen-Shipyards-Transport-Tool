from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import GroundShipment
# Register your models here.
admin.site.register(GroundShipment, ImportExportModelAdmin)


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
