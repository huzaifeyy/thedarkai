from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

cardata =['RO14LCJ', '6OY']
toprint=[]

for counter in range(len(cardata)):   
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://vehicleenquiry.service.gov.uk/?_ga=2.90516829.698756013.1596820709-2077825283.1588703682")
    driver.maximize_window() 
    username = driver.find_element_by_name("wizard_vehicle_enquiry_capture_vrn[vrn]")
    sleep(2)
    username.send_keys(cardata[counter])
    username.send_keys(Keys.ENTER)
    sleep(3)
    button = driver.find_element_by_id("yes-vehicle-confirm").click()
    sleep(3)
    button2 = driver.find_element_by_id("capture_confirm_button").click()
    sleep(5)
    toprint = driver.find_element_by_xpath("/html[@class='govuk-template']/body[@class='govuk-template__body js-enabled']/div[@class='govuk-width-container']/main[@id='main-content']/div[@class='govuk-grid-row'][2]/div[@class='govuk-grid-column-one-half'][1]/div[@class='govuk-panel govuk-panel--confirmation govuk-panel--fixed-height']/div[@class='govuk-!-font-size-24 govuk-panel__body']/strong[@class='white'][2]")
    toprint2 = driver.find_element_by_xpath("/html[@class='govuk-template']/body[@class='govuk-template__body js-enabled']/div[@class='govuk-width-container']/main[@id='main-content']/div[@class='govuk-grid-row'][2]/div[@class='govuk-grid-column-one-half'][2]/div[@id='mot-status-panel']/div[@class='govuk-!-font-size-24 govuk-panel__body']/strong[@class='white'][2]")
    stringtoprint= str(counter+1) + '.' + str(cardata[counter])
    print(stringtoprint)
    print("  TAX is due ", toprint.text)
    print("  MOT is due ", toprint2.text)
    driver.close()
    





