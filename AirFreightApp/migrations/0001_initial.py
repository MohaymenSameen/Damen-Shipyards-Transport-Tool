# Generated by Django 3.2 on 2021-05-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirFreightShipment',
            fields=[
                ('MasterOrder', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('ShipmentNr', models.DecimalField(decimal_places=6, max_digits=15)),
                ('RPShipmentNr', models.TextField(blank=True, max_length=30, null=True)),
                ('SenderName', models.TextField(blank=True, max_length=100, null=True)),
                ('ReceiverName', models.TextField(blank=True, max_length=100, null=True)),
                ('Country', models.TextField(blank=True, max_length=30, null=True)),
                ('City', models.TextField(blank=True, max_length=30, null=True)),
                ('ZipCode', models.TextField(blank=True, max_length=7, null=True)),
                ('CosigneeReference', models.TextField(blank=True, max_length=20, null=True)),
                ('OrderNrCosignee', models.TextField(blank=True, max_length=20, null=True)),
                ('ShipmentInfo', models.TextField(blank=True, max_length=20, null=True)),
                ('ShipmentDate', models.DateField(blank=True, null=True)),
                ('ETD', models.DateField(blank=True, null=True)),
                ('ETA', models.DateField(blank=True, null=True)),
                ('Status', models.TextField()),
            ],
        ),
    ]
