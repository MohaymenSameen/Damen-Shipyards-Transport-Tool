from django.db import models


# Create your models here.
class AirFreightShipment(models.Model):
    MasterOrder = models.TextField(primary_key=True, max_length=20)
    ShipmentNr = models.DecimalField(max_digits=15, decimal_places=6)
    RPShipmentNr = models.TextField(max_length=30, blank=True, null=True)
    SenderName = models.TextField(max_length=100, blank=True, null=True)
    ReceiverName = models.TextField(max_length=100, blank=True, null=True)
    Country = models.TextField(max_length=30, blank=True, null=True)
    City = models.TextField(max_length=30, blank=True, null=True)
    ZipCode = models.TextField(max_length=7, blank=True, null=True)
    CosigneeReference = models.TextField(max_length=20, blank=True, null=True)
    OrderNrCosignee = models.TextField(max_length=20, blank=True, null=True)
    ShipmentInfo = models.TextField(max_length=20, blank=True, null=True)
    ShipmentDate = models.DateField(blank=True, null=True)
    ETD = models.DateField(blank=True, null=True)
    ETA = models.DateField(blank=True, null=True)
    Status = models.TextField()
