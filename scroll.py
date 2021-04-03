from selenium import webdriver
import time

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://www.countries-ofthe-world.com/flags-of-the-world.html'

driver.get(url)
driver.maximize_window()

# Scroll down page by pixel
# driver.execute_script('window.scrollBy(0,1000)', '')

# Scroll down to page till the element is visible
# flag = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[48]/td[1]/img')
# driver.execute_script('arguments[0].scrollIntoView();', flag)

# Scroll down to the end of the page
driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
time.sleep(5)
driver.quit()