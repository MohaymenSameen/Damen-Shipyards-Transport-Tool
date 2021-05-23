# Generated by Django 3.2 on 2021-05-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OceanFreightShipment',
            fields=[
                ('ShipmentId', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('ContainerNr', models.TextField(blank=True, null=True)),
                ('Departure', models.CharField(max_length=50)),
                ('Destination', models.CharField(max_length=100)),
                ('ScheduledDeparture', models.DateTimeField()),
                ('ScheduledArrival', models.DateTimeField()),
                ('RevisedArrival', models.DateTimeField(blank=True, null=True)),
                ('TotalVolume', models.DecimalField(blank=True, decimal_places=3, max_digits=10000, null=True)),
                ('TotalWeight', models.IntegerField(blank=True, null=True)),
                ('Dimensions', models.CharField(blank=True, max_length=50, null=True)),
                ('Carrier', models.CharField(max_length=50)),
                ('ShipperReference', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]