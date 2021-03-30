from selenium import webdriver
from selenium.webdriver.common.by import By

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://london.com'

driver.get(url)

# Find all element by tag name
links = driver.find_elements(By.TAG_NAME, 'a')

print(f'Number of links present: {len(links)}')

# Print the Link Text
for link in links:
    print(link.text)

# Click on a link
#driver.find_element(By.LINK_TEXT, 'London Map').click()

# Click on a partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, 'Lon').click()

