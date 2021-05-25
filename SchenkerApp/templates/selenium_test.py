import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
listId = ["27690040156446", "52890011591955"]
listShipment = list()

# Click ok to cookies
driver.get("https://eschenker.dbschenker.com/app/tracking-public/?refNumber=" + listId[0])
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//button[@class='mat-focus-indicator primary mat-button mat-button-base']").click()
for shipmentId in listId:
    driver.get("https://eschenker.dbschenker.com/app/tracking-public/?refNumber=" + shipmentId)
    driver.implicitly_wait(3)  # seconds

    arrival = driver.find_element_by_xpath("//span[@data-test='scheduled_arrival_value']").text
    departurePort = driver.find_element_by_xpath("//span[@data-test='departure_value']").text
    destinationPort = driver.find_element_by_xpath("//span[@data-test='destination_value']").text
    ETD = driver.find_element_by_xpath("//span[@data-test='scheduled_departure_value']").text
    ETA = driver.find_element_by_xpath("//span[@data-test='scheduled_arrival_value']").text
    revisedArrival = driver.find_element_by_xpath("//span[@data-test='revised_arrival_value']").text
    totalVolume = driver.find_element_by_xpath("//span[@data-test='total_volume_value']").text
    totalWeight = driver.find_element_by_xpath("//span[@data-test='total_weight_value']").text
    carrier = driver.find_element_by_xpath("//span[@data-test='carrier_value']").text
    containers = driver.find_elements_by_xpath("//span[@data-test='container_value']")
    for container in containers:
        listShipment.append([shipmentId, container.text, departurePort, destinationPort, ETD, ETA, revisedArrival,
                             totalVolume, totalWeight, carrier])
    # listShipment = np.array([[shipmentId, containerList[0], departurePort, destinationPort, ETD, ETA, revisedArrival,
    #                           totalVolume, totalWeight, carrier]])
df = pd.DataFrame(listShipment,
                  columns=["ShipmentId", "ContainerNr", "Departure", "Destination", "ScheduledDeparture",
                           "ScheduledArrival", "RevisedArrival", "TotalVolume", "TotalWeight", "Carrier"])
df.insert(0, 'ID', '')
df.to_excel("selenium.xlsx", index=False, encoding='utf8')
driver.close()
