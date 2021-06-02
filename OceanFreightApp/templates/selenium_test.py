import numpy as np
import pandas as pd
from selenium import webdriver
from datetime import datetime
import os.path
from damen_django_project.settings import BASE_DIR

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

location = os.path.join(BASE_DIR, "resources", "Schenker Sea 2020-2021.xlsx")

df = pd.read_excel(location)
listId = df[['STT']].drop_duplicates().to_numpy()

driver = webdriver.Chrome()
listShipment = list()

# Click ok to cookies
driver.get("https://eschenker.dbschenker.com/app/tracking-public/?refNumber=" + str(listId[0][0].item()))
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//button[@class='mat-focus-indicator primary mat-button mat-button-base']").click()


def read_data():
    arrival = driver.find_element_by_xpath("//span[@data-test='scheduled_arrival_value']").text
    departurePort = driver.find_element_by_xpath("//span[@data-test='departure_value']").text
    destinationPort = driver.find_element_by_xpath("//span[@data-test='destination_value']").text

    ETD = driver.find_element_by_xpath("//span[@data-test='scheduled_departure_value']").text
    ETA = driver.find_element_by_xpath("//span[@data-test='scheduled_arrival_value']").text
    revisedArrival = driver.find_element_by_xpath("//span[@data-test='revised_arrival_value']").text
    if ETD == "-":
        return
    # New Format Date Time
    ETD = datetime.strptime(ETD, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")
    ETA = datetime.strptime(ETA, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")
    if revisedArrival != "-":
        revisedArrival = datetime.strptime(revisedArrival, '%Y/%m/%d %H:%M').strftime("%Y-%m-%d")

    totalVolume = driver.find_element_by_xpath("//span[@data-test='total_volume_value']").text
    totalWeight = driver.find_element_by_xpath("//span[@data-test='total_weight_value']").text
    totalVolume = totalVolume.replace(' CBM', '')
    totalWeight = totalWeight.replace(' KGS', '')

    carrier = driver.find_element_by_xpath("//span[@data-test='carrier_value']").text
    containers = driver.find_elements_by_xpath("//span[@data-test='container_value']")

    for container in containers:
        listShipment.append([shipmentId, container.text, departurePort, destinationPort, ETD, ETA, revisedArrival,
                             totalVolume, totalWeight, carrier])


for shipmentId in listId:
    shipmentId = str(shipmentId.item())
    driver.get("https://eschenker.dbschenker.com/app/tracking-public/?refNumber=" + shipmentId)
    driver.implicitly_wait(3)  # seconds
    try:
        # Shipment not found
        driver.find_element_by_xpath("//h5[@class='error ng-star-inserted']")
    except NoSuchElementException:
        read_data()

df = pd.DataFrame(listShipment,
                  columns=["ShipmentId", "ContainerNr", "Departure", "Destination", "ScheduledDeparture",
                           "ScheduledArrival", "RevisedArrival", "TotalVolume", "TotalWeight", "Carrier"])
df.insert(0, 'ID', '')
df.to_excel("selenium.xlsx", index=False, encoding='utf8')
driver.close()
