from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://practice.automationtesting.in/'

driver.get(url)

driver.implicitly_wait(10)

assert 'Automation Practice Site' in driver.title

driver.find_element_by_id('menu-item-50').click()
driver.find_element_by_id('username').send_keys('mercury')
driver.find_element_by_id('password').send_keys('mercury')

rememberme_chkbox = driver.find_element_by_id('rememberme').is_selected()
print(f'before click: {rememberme_chkbox}')
driver.find_element_by_id('rememberme').click()
print(f'before click: {rememberme_chkbox}')


driver.find_element_by_name('login').click()