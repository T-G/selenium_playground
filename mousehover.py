from selenium import webdriver
from selenium.webdriver import ActionChains

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://opensource-demo.orangehrmlive.com/'

driver.get(url)

driver.find_element_by_id('txtUsername').send_keys('Admin')
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

admin = driver.find_element_by_id('menu_admin_viewAdminModule')
user_management = driver.find_element_by_id('menu_admin_UserManagement')
users = driver.find_element_by_id('menu_admin_viewSystemUsers')

# Mouse over Action
# Create an object of the ActionChain class by padding the driver in the construcor
actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()