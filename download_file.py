from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': '/home/theo/Downloads/Test'})


browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location, chrome_options=chrome_options)

url = r'http://demo.automationtesting.in/FileDownload.html'

driver.get(url)

driver.maximize_window()

# Download TEXT file
driver.find_element_by_id('textbox').send_keys('Some text input from user')
driver.find_element_by_id('createTxt').click()
driver.find_element_by_id('link-to-download').click()

time.sleep(3)
# Download PDF file
driver.find_element_by_id('pdfbox').send_keys('Some pdf input from user')
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()

driver.close()

