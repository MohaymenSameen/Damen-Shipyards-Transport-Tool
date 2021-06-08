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
        # ETA
        column[22] = driver.find_element_by_xpath("//div[@class='c-tracking-result--status-copy-date  ']").text
        listInfo = driver.find_elements_by_xpath(
            "//h4[@class='c-tracking-result--checkpoint--date  l-grid--w-100pc-s']")
        # ETC
        column[21] = listInfo[-1].text


def getDbSchenker(column):
    ETD = driver.find_element_by_xpath("//span[@data-test='scheduled_departure_value']").text
    ETA = driver.find_element_by_xpath("//span[@data-test='scheduled_arrival_value']").text
    revisedArrival = driver.find_element_by_xpath("//span[@data-test='revised_arrival_value']").text

    driver.find_element_by_xpath("//h5[@data-test='shipment_status_history_label']").click()
    status = driver.find_elements_by_xpath("//td[@data-label='Event']")
    status = status[-1].text
    column[1] = status

    if ETD == "-" or ETA == "-":
        return
    # New Format Date Time
    ETD = datetime.strptime(ETD, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")
    ETA = datetime.strptime(ETA, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")
    column[21] = ETD
    column[22] = ETA
    if revisedArrival != "-":
        revisedArrival = datetime.strptime(revisedArrival, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")
        column[22] = revisedArrival


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
    elif column[20] == "DB Schenker":
        driver.get("https://eschenker.dbschenker.com/app/tracking-public/?refNumber=" + str(column[2]))
        try:
            iframe = driver.find_element_by_tag_name('iframe')
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath(
                "//button[@class='mat-focus-indicator primary mat-button mat-button-base']").click()
            getDbSchenker(column)
        except:
            try:
                getDbSchenker(column)
            except:
                continue
    elif column[20] == "Fedex":
        # Pending 784098044813
        driver.get("https://www.fedex.com/fedextrack/?action=track&trackingnumber=" + str(column[2]))
        try:
            status = driver.find_element_by_xpath("//h3[@data-test-id='key-status']").text
            # driver.find_element_by_xpath("//span[@data-test-id='delivery-date-text']").text
            if status == "Pending":
                column[1] = status
                continue
            else:
                driver.find_element_by_xpath("//button[@id='tab-list-item-tab_panel_3']").click()
                xlist = driver.find_elements_by_xpath("//div[@class='key-value-list__value color-gray-5']")
                ETD = xlist[4].text
                ETA = xlist[5].text
                ETA = ETA.replace('at ','')
                ETA = ETA.replace('21','2021')

                ETA = datetime.strptime(ETA, '%m/%d/%Y %I:%M %p').strftime("%Y-%m-%d %H:%M")
                ETD = ETD.replace(' Ship Date Tooltip','')
                ETD = ETD.replace('21','2021')
                ETD = datetime.strptime(ETD, '%m/%d/%Y').strftime("%Y-%m-%d %H:%M")
                column[21] = ETD
                column[22] = ETA
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
