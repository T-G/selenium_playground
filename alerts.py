from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://testautomationpractice.blogspot.com/'

driver.get(url)

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(3)

#driver.switch_to_alert().accept() # closes the alert window by using Ok button
driver.switch_to_alert().dismiss() # closes the alert window using Cancel button
