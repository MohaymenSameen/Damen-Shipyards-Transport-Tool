# Generated by Django 3.2 on 2021-05-14 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundShippingApp', '0004_alter_groundshipment_deliverycompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groundshipment',
            name='ETA',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
