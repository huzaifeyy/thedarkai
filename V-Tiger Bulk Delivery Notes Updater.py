from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import time




driver = webdriver.Chrome('./chromedriver')
driver.get("https://erp.koolmaxgroup.com/index.php?module=ITS4YouDeliveryNotes&parent=&page=1&view=List&viewname=85&orderby=&sortorder=&search_params=&search_key=deliverynotes_no&search_value=")
driver.maximize_window()
sleep(3)
username = driver.find_element_by_name('username')
sleep(2)
username.send_keys('habib')
sleep(3)
password = driver.find_element_by_name('password')
sleep(3)
password.send_keys('habib123')
sleep(3)
password.send_keys(Keys.ENTER)
sleep(3)
for counter in range(100):
    start = time.time()
    auto = driver.find_element_by_xpath("/html/body/div[@id='page']/div[@class='bodyContents']/div[@class='mainContainer row-fluid']/div[@id='rightPanel']/div[@class='listViewPageDiv']/div[@id='listViewContents']/div[@class='listViewEntriesDiv contents-bottomscroll']/div[@class='bottomscroll-div']/table[@class='table table-bordered listViewEntriesTable']/tbody/tr[@id='ITS4YouDeliveryNotes_listView_row_1']/td[@class='listViewEntryValue medium'][1]").click()
    sleep(3)
    auto2 = driver.find_element_by_xpath("/html/body/div[@id='page']/div[@class='bodyContents']/div[@class='mainContainer row-fluid']/div[@id='rightPanel']/div[@class='detailViewContainer']/div[@class='row-fluid detailViewTitle']/div[@class=' span10 ']/div[@class='row-fluid'][1]/div[@class='span7']/div[@class='pull-right detailViewButtoncontainer']/div[@class='btn-toolbar']/span[@class='btn-group'][1]/button[@class='btn btn-success actiondeliver']/strong").click()
    sleep(3)
    auto3 = driver.find_element_by_xpath("/html/body[@class='modal-open']/div[@class='blockUI blockMsg blockPage']/div[@id='globalmodal']/div[@class='modelContainer']/form[@id='ChangeStatusDeliverActionForm']/div[@class='modal-footer quickCreateActions']/button[@class='btn btn-success']/strong").click()
    sleep(3)
    auto4 = driver.find_element_by_xpath("/html/body/div[@id='page']/div[@class='navbar navbar-fixed-top  navbar-inverse noprint']/div[@id='topMenus']/div[@id='nav-inner']/div[@class='menuBar row-fluid']/div[@class='span9']/ul[@id='largeNav']/li[@class='tabs'][8]/a[@id='menubar_item_ITS4YouDeliveryNotes']").click()
    end = time.time()
    print(end - start)
