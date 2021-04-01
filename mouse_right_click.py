from selenium import webdriver
from selenium.webdriver import ActionChains

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://swisnl.github.io/jQuery-contextMenu/demo.html'

driver.get(url)

driver.maximize_window()
btn = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

actions = ActionChains(driver)
actions.context_click(btn).perform()