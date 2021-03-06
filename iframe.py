from selenium import webdriver
import time

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html'

driver.get(url)

# select the first frame
driver.switch_to.frame('packageListFrame')
# select a link in the frame
driver.find_element_by_link_text('org.openqa.selenium').click()
time.sleep(3)

# go back to the page
driver.switch_to.default_content()

# switch to second frame
driver.switch_to.frame('packageFrame')
driver.find_element_by_link_text('WebDriver').click()
# go back to the page
time.sleep(3)

driver.switch_to.default_content()

# switch to third frame
driver.switch_to.frame('classFrame')
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]').click()
