from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://www.expedia.com/'

driver.implicitly_wait(5)
driver.maximize_window() #Display full width page
driver.get(url)

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

time.sleep(2) # from python

driver.find_element_by_css_selector('button[data-stid=location-field-leg1-origin-menu-trigger]').send_keys('NYC') #Origin
time.sleep(2)
driver.find_element_by_css_selector('button[data-stid=location-field-leg1-destination-menu-trigger]').send_keys('LHR') #Destination

#driver.find_element(By.ID, 'd1-btn').click() # clear the input text
#driver.find_element(By.ID, 'd1').clear() # clear the input text

driver.find_element_by_css_selector('button[data-testid=submit-button').click()

# Explicit wait
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stopFilter-0"]')))
#
# element.click()
# time.sleep(3)
driver.quit()