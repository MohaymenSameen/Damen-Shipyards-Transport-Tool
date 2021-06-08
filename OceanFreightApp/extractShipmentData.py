import os.path
from damen_django_project.settings import BASE_DIR
import pandas as pd

location = os.path.join(BASE_DIR, "resources", "Schenker Sea 2020-2021.xlsx")
df = pd.read_excel(location)

# Adding new Id to concatenate shipment Id and container number to give a unique primary key
df["MainShipmentId"] = df['STT'].map(str) + df['Container No'].map(str)

# Removing Spaces
df["MainShipmentId"] = df["MainShipmentId"].str.replace(' ', '')

selectColumns = df[
    ['MainShipmentId', 'STT', 'Container No', 'Departure Port', 'Destination Port', 'ETD Date (GMT Time)',
     'ETA Date (GMT Time)',
     'CTA Date (GMT Time)', 'Container Volume', 'Container Weight', 'Container Movement', 'Carrier',
     'Shipper Reference']]

renameColumns = selectColumns.rename(
    columns={"STT": "ShipmentId", "Container No": "ContainerNr", "Departure Port": "Departure",
             "Destination Port": "Destination", "ETD Date (GMT Time)": "ScheduledDeparture",
             "ETA Date (GMT Time)": "ScheduledArrival", "CTA Date (GMT Time)": "RevisedArrival",
             "Container Volume": "TotalVolume", "Container Weight": "TotalWeight", "Container Movement": "Dimensions",
             "Carrier": "Carrier", "Shipper Reference": "ShipperReference"})

newExcel = renameColumns.to_excel("CleanOceanFreightDataset.xlsx", index=False, encoding='utf8')
