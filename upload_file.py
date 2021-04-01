from selenium import webdriver

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://testautomationpractice.blogspot.com/'

driver.get(url)

driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element_by_id('RESULT_FileUpload-10').send_keys(r'/home/theo/Downloads/pexels-anna-shvets-3845766.jpg')
