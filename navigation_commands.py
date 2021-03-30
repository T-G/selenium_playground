from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=browser_driver_location)

url1 = r'http://newtours.demoaut.com/'
url2 = r'http://pavantestingtools.blogspot.in/'

driver.get(url1) #FR
print(f'Current Page URL: {driver.current_url}')
print(f'Page Title: {driver.title}')

time.sleep(5)
driver.get(url2) #TT testing tools
print(f'Current Page URL: {driver.current_url}')
print(f'Page Title: {driver.title}')

driver.back() # Go to history page
time.sleep(5)
print(f'Current Page URL: {driver.current_url}')
print(f'Page Title: {driver.title}') #FB

driver.forward() # Go to Current Page
time.sleep(5)
print(f'Current Page URL: {driver.current_url}')
print(f'Page Title: {driver.title}') #TT

