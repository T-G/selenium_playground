from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://demo.automationtesting.in'

driver.get(url)

# Go to the login Page
driver.find_element_by_xpath('//*[@id="btn1"]').click()

# Check if the email and password field is enabled
password_ele = driver.find_element_by_xpath('/html/body/div/div/div[3]/input')
print(f'Password field is displayed: {password_ele.is_displayed()}') # returns True or False based on the element status
print(f'Password field is enabled: {password_ele.is_enabled()}') # returns True or False

email_ele = driver.find_element_by_xpath('/html/body/div/div/div[2]/input')
print(f'Email field is displayed: {email_ele.is_displayed()}')
print(f'Email field is enabled: {email_ele.is_enabled()}')

# Perform the login
email_ele.send_keys('mercury')
password_ele.send_keys('mercury')

#trip_radio_btn = driver.find_element_by_css_selector('input[value=roundtrip').is_selected()

driver.find_element_by_id('enterbtn').click()