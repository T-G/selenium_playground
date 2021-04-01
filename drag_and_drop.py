from selenium import webdriver
from selenium.webdriver import ActionChains

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'

driver.get(url)

driver.maximize_window()

# identify source and targer elements
src_element = driver.find_element_by_xpath('//*[@id="box1"]')
target_element = driver.find_element_by_xpath('//*[@id="box101"]')

actions = ActionChains(driver)
actions.drag_and_drop(src_element, target_element).perform()