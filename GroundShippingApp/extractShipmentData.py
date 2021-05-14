import os.path
from damen_django_project.settings import BASE_DIR
import pandas as pd

# from .models import Shipment

location = os.path.join(BASE_DIR, "resources", "Courier 2021.1.xls")

df = pd.read_excel(location)

# df['Shipmentdate'] = pd.to_datetime(df['Shipmentdate'], format='%d/%M/%Y').dt.strftime('%Y-%m-%d')
# df['ETD'] = pd.to_datetime(df['ETD'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')
# df['ETA'] = pd.to_datetime(df['ETA'], format='%d/%M/%Y', errors='coerce').dt.strftime('%Y-%m-%d')

df['Dimensions'] = df['Length'].map(str) + 'L-' + df['Width'].map(str) + 'W-' + df['Height'].map(str) + 'H'

selectColumns = df[
    ['Order No.', 'Status', 'Tracking No.', 'Contents', 'Weight', 'Dimensions', 'Collection Address Company Name',
     'Collection Address Name', 'Collection Address Address',
     'Collection Address Postal Code/ZIP', 'Collection Address City', 'Delivery Address Company Name',
     'Delivery Address Name', 'Delivery Address Address', 'Delivery Address Address Line 2',
     'Delivery Address Postal Code/ZIP', 'Delivery Address City',
     'Delivery Address Country', 'Reference', 'Consignment No.', 'Courier', 'ETC', 'ETA']]

renameColumns = selectColumns.rename(
    columns={"Order No.": "OrderNr", "Status": "Status", "Tracking No.": "TrackingNr",
             "Contents": "Contents", "Weight": "Weight",
             "Dimensions": "Dimensions", "Collection Address Company Name": "CollectionCompany",
             "Collection Address Name": "CollectionName", "Collection Address Address": "CollectionAddress",
             "Collection Address Postal Code/ZIP": "CollectionZipCode",
             "Collection Address City": "CollectionCity", "Delivery Address Company Name": "DeliveryCompany",
             "Delivery Address Name": "DeliveryName", "Delivery Address Address": "DeliveryAddress1",
             "Delivery Address Address Line 2": "DeliveryAddress2",
             "Delivery Address Postal Code/ZIP": "DeliveryZipCode",
             "Delivery Address City": "DeliveryCity",
             "Delivery Address Country": "DeliveryCountryCode",
             "Reference": "Reference",
             "Consignment No.": "CosigneeNr",
             "Courier": "Courier",
             "ETC": "ETC", "ETA": "ETA"})

renameColumns.insert(0, 'ID', '')
newExcel = renameColumns.to_excel("CleanGroundShippingDataset.xlsx", index=False, encoding='utf8')
