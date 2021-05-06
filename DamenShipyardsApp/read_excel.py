import pandas as pd

df = pd.read_excel(r'../resources/Damen_Shipments.xlsx')

#print(df.sort_values('Shipment ID', ascending=True))

groupBy = df.groupby("Forwarder ID")

count = groupBy['Shipment ID'].count()

print(count.sort_values(ascending=False))






