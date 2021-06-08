import os.path
from damen_django_project.settings import BASE_DIR
import pandas as pd

# from .models import Shipment

location = os.path.join(BASE_DIR, "resources", "Rhenus Air 2021 Shipments.xls")

df = pd.read_excel(location)

df['BriefStatus'] = df['Status']

df['BriefStatus'].replace(['Shipment delivered to consignee', 'Shipment departed from airport of origin',
                           'Shipment handed over to another forwarder', 'Customs clearance completed',
                           'Rejected declaration (by customs)', 'Consignee is a self-collector',
                           'Shipment arrived at import gateway', 'Confirmation of exit received',
                           'Shipment handed over to destination forwarder', 'Departure is checked',
                           'Shipment booked on flight:', 'Shipment picked up',
                           'Arrival Notice provided to customer/notify', 'Customer order received and file opened',
                           'Shipment discrepancy - consignee or agent has been informed of arrival',
                           'Shipment arrived at airport of destination',
                           'Shipment departed from export gateway', 'Booking changed - order changed by principal',
                           '(X)FWB received by carrier', 'Shipment delayed - flight departure delayed',
                           'Arrival at exit', 'Shipment prepared for loading by carrier',
                           'Shipment arrived at departure carrier', 'Shipment arrived at transit airport'],
                          ['Delivered', 'Departed', 'Arranged', 'In Transit', 'Rejected', 'Self-Collection',
                           'Arrived', 'In Transit', 'In Transit', 'Departed', 'In Transit', 'Collected',
                           'Status Update To Customer', 'Delivered', 'Delayed', 'In Transit', 'Departed',
                           'Booking Changed', 'Collected', 'Delayed', 'In Transit', 'In Transit', 'In Transit',
                           'In Transit'], inplace=True)

df['Shipmentdate'] = pd.to_datetime(df['Shipmentdate'], format='%d/%M/%Y').dt.strftime('%Y-%m-%d')
df['ETD'] = pd.to_datetime(df['ETD'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
df['ETA'] = pd.to_datetime(df['ETA'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

selectColumns = df[
    ['Masterorder/Reference', 'Shipmentno', 'RP Shipmentno', 'Sender Name', 'Receiver Name', 'Country',
     'Zip Code', 'City', 'Consignee Reference', 'Order no. Consignor', 'Shipment Info',
     'Shipmentdate', 'ETD', 'ETA', 'Status', 'BriefStatus']]

renameColumns = selectColumns.rename(
    columns={"Masterorder/Reference": "MasterOrder", "Shipmentno": "ShipmentNr", "RP Shipmentno": "RPShipmentNr",
             "Sender Name": "SenderName", "Receiver Name": "ReceiverName",
             "Country": "Country", "City": "City",
             "Zip Code": "ZipCode", "Consignee Reference": "CosigneeReference",
             "Order no. Consignor": "OrderNrCosignee",
             "Shipment Info": "ShipmentInfo", "Shipmentdate": "ShipmentDate", "ETD": "ETD", "ETA": "ETA",
             "Status": "Status", "BriefStatus": "BriefStatus"})

newExcel = renameColumns.to_excel("cleanAirFreightDataset.xlsx", index=False, encoding='utf8')
