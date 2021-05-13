import os.path
from damen_django_project.settings import BASE_DIR
import pandas as pd

# from .models import Shipment

location = os.path.join(BASE_DIR, "resources", "Rhenus Air 2021 Shipments.xls")

df = pd.read_excel(location)

df['Shipmentdate'] = pd.to_datetime(df['Shipmentdate'], format='%d/%M/%Y').dt.strftime('%Y-%m-%d')
df['ETD'] = pd.to_datetime(df['ETD'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
df['ETA'] = pd.to_datetime(df['ETA'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

selectColumns = df[
    ['Masterorder/Reference', 'Shipmentno', 'RP Shipmentno', 'Sender Name', 'Receiver Name', 'Country',
     'Zip Code', 'City', 'Consignee Reference', 'Order no. Consignor', 'Shipment Info',
     'Shipmentdate', 'ETD', 'ETA', 'Status']]

renameColumns = selectColumns.rename(
    columns={"Masterorder/Reference": "MasterOrder", "Shipmentno": "ShipmentNr", "RP Shipmentno": "RPShipmentNr",
             "Sender Name": "SenderName", "Receiver Name": "ReceiverName",
             "Country": "Country", "City": "City",
             "Zip Code": "ZipCode", "Consignee Reference": "CosigneeReference",
             "Order no. Consignor": "OrderNrCosignee",
             "Shipment Info": "ShipmentInfo", "Shipmentdate": "ShipmentDate", "ETD": "ETD", "ETA": "ETA",
             "Status": "Status"})

renameColumns.insert(0, 'ID', '')
newExcel = renameColumns.to_excel("cleanAirFreightDataset.xlsx", index=False, encoding='utf8')
