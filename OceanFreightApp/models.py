from django.db import models


# Create your models here.
class OceanFreightShipment(models.Model):
    ShipmentId = models.PositiveBigIntegerField(primary_key=True)
    ContainerNr = models.TextField(blank=True, null=True)
    Departure = models.CharField(max_length=50)
    Destination = models.CharField(max_length=100)
    ScheduledDeparture = models.DateTimeField()
    ScheduledArrival = models.DateTimeField()
    RevisedArrival = models.DateTimeField(blank=True, null=True)
    TotalVolume = models.DecimalField(decimal_places=3,max_digits=10000, blank=True, null=True)
    TotalWeight = models.IntegerField(blank=True, null=True)
    Dimensions = models.CharField(max_length=50, blank=True, null=True)
    Carrier = models.CharField(max_length=50)
    ShipperReference = models.CharField(max_length=20, blank=True, null=True)
