from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
driver = webdriver.Chrome(executable_path=driver_location)

#driver_location = r'/home/theo/Workspace/browsersDriver/geckodriver'
#driver = webdriver.Firefox(executable_path=driver_location)

driver.get('https://londonreservation.com')
print(f'Page URL: {driver.current_url}') # returns the URL of the page
print(f'Page title: {driver.title}') # Get page Title
#print(driver.page_source) # returns the HTML code for the page
driver.close() # close the browser



