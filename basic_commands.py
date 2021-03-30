from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://demo.automationtesting.in/Windows.html'

driver.get(url)

print(f'Current Page URL: {driver.current_url}')
print(f'Page Title: {driver.title}')

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)
driver.close() # close the currently focused browser
driver.quit() # close all the browsers