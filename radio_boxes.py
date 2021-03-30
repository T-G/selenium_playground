from selenium import webdriver
from selenium.webdriver.common.by import By

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'

driver.get(url)

male_radio_button = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected() # True or False
female_radio_button = driver.find_element_by_id('RESULT_RadioButton-7_1').is_selected() # True or False
print(f'Male radio is selected: {male_radio_button}')
print(f'Female radio is selected: {female_radio_button}')

driver.find_element_by_css_selector('label[for=RESULT_RadioButton-7_0]').click()

# working with check boxes
driver.find_element_by_css_selector('label[for=RESULT_CheckBox-8_0]').click()
driver.find_element_by_css_selector('label[for=RESULT_CheckBox-8_1]').click()
driver.find_element_by_css_selector('label[for=RESULT_CheckBox-8_2]').click()
