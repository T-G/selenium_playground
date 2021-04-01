from selenium import webdriver
from selenium.webdriver import ActionChains

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://testautomationpractice.blogspot.com/'

driver.get(url)

driver.maximize_window()
btn_element = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

actions = ActionChains(driver)
actions.double_click(btn_element).perform() # perform double click action