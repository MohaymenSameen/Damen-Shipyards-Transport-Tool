import os.path

from selenium.common.exceptions import NoSuchElementException

from damen_django_project.settings import BASE_DIR
import pandas as pd
from selenium import webdriver
from datetime import datetime
import os.path

# from .models import Shipment

location = os.path.join(BASE_DIR, "resources", "Courier 2021.1.xls")

df = pd.read_excel(location)
driver = webdriver.Chrome()
df['Dimensions'] = df['Length'].map(str) + 'L-' + df['Width'].map(str) + 'W-' + df['Height'].map(str) + 'H'

selectColumns = df[
    ['Order No.', 'Status', 'Tracking No.', 'Contents', 'Weight', 'Dimensions', 'Collection Address Company Name',
     'Collection Address Name', 'Collection Address Address',
     'Collection Address Postal Code/ZIP', 'Collection Address City', 'Delivery Address Company Name',
     'Delivery Address Name', 'Delivery Address Address', 'Delivery Address Address Line 2',
     'Delivery Address Postal Code/ZIP', 'Delivery Address City',
     'Delivery Address Country', 'Reference', 'Consignment No.', 'Courier', 'ETC', 'ETA']]
selectColumns = selectColumns.to_numpy()


def getDataDHL(column):
    if driver.find_element_by_xpath("//h1[@class='l-grid--w-100pc-s']").text == 'TRACK: PARCEL':
        column[22] = driver.find_element_by_xpath("//div[@class='c-tracking-result--status-copy-date  ']").text
        listInfo = driver.find_elements_by_xpath(
            "//h4[@class='c-tracking-result--checkpoint--date  l-grid--w-100pc-s']")
        column[21] = listInfo[-1].text


for column in selectColumns:
    if column[20] == "DHL":
        driver.get(
            "https://www.dhl.com/nl-en/home/tracking/tracking-parcel.html?submit=1&tracking-id=" + str(column[2]))
        driver.implicitly_wait(5)  # seconds
        try:
            driver.find_element_by_xpath("//button[@id='accept-recommended-btn-handler']").click()
            getDataDHL(column)
        except:
            try:
                getDataDHL(column)
            except:
                continue

driver.close()

df = pd.DataFrame(selectColumns,
                  columns=["OrderNr", "Status", "TrackingNr", "Contents",
                           "Weight", "Dimensions", "CollectionCompany", "CollectionName",
                           "CollectionAddress", "CollectionZipCode", "CollectionCity", "DeliveryCompany",
                           "DeliveryName", "DeliveryAddress1", "DeliveryAddress2", "DeliveryZipCode",
                           "DeliveryCity", "DeliveryCountryCode", "Reference", "CosigneeNr", "Courier", "ETC", "ETA"])

df.to_excel("selenium_ground.xlsx", index=False, encoding='utf8')

# array(['SA1321541', 'Delivered', 4163486515, 'Documents', 0.1,
#        'Damen Shipyards Gorinchem B.V.', 'Arend De Reus',
#        'Avelingen Oost 12', '4202 MN', 'Gorinchem',
#        'Damen Shipyards Sharjah FZE', 'Suresh Lamba',
#        'Inside Hamriyah Free Zone,', 'Plot Hd-22 Po Box.52125', nan,
#        'Sharjah', 'AE', '21948.3/S233648+/143754+', 4163486515, 'DHL',
#        '2021-01-04 18:00:00', '2021-01-06 23:00:00'], dtype=object)
