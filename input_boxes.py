from selenium import webdriver
from selenium.webdriver.common.by import By

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'

driver.get(url)

input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(input_boxes)) # 6

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print(f'Input field displayed or not: {status}')

status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print(f'Input field enabled or not: {status}')

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Theo')

driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('Gomes')
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('02077458896')
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys('UK')
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys('London')
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys('Theo@gmail.com')