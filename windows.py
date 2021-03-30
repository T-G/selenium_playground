from selenium import webdriver
from selenium.webdriver.common.by import By

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)
url = 'http://demo.automationtesting.in/Windows.html'
driver.get(url)

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

# Get handle value of the current window
print(f'Hashcode for parent window: {driver.current_window_handle}')

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == 'Frames & windows':
        driver.close() # Close the parent window
    print(f'Window hashcode: {handle}')

driver.quit()