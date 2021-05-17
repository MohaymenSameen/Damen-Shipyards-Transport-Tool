from django.db import models


# Create your models here.
class GroundShipment(models.Model):
    OrderNr = models.TextField(primary_key=True, max_length=9)
    Status = models.TextField(max_length=20)
    TrackingNr = models.TextField(max_length=14)
    Contents = models.TextField(max_length=50)
    Weight = models.DecimalField(max_digits=1000, decimal_places=2)
    Dimensions = models.TextField(max_length=20)
    CollectionCompany = models.TextField(max_length=50)
    CollectionName = models.TextField(max_length=30)
    CollectionAddress = models.TextField(max_length=20)
    CollectionZipCode = models.TextField(max_length=7)
    CollectionCity = models.TextField(max_length=50)
    DeliveryCompany = models.TextField(max_length=50, blank=True, null=True)
    DeliveryName = models.TextField(max_length=30)
    DeliveryAddress1 = models.TextField(max_length=20)
    DeliveryAddress2 = models.TextField(max_length=20, blank=True, null=True)
    DeliveryZipCode = models.TextField(max_length=7, blank=True, null=True)
    DeliveryCity = models.TextField(max_length=50)
    DeliveryCountryCode = models.TextField(max_length=2)
    Reference = models.TextField(max_length=20)
    Courier = models.TextField(max_length=20)
    CosigneeNr = models.TextField(max_length=14)
    ETC = models.DateTimeField()
    ETA = models.DateTimeField(blank=True, null=True)
