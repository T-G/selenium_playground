from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'

driver.get(url)

target_element = driver.find_element_by_id('RESULT_RadioButton-9')
dropdown_box = Select(target_element)

# Select by visible text
#dropdown_box.select_by_visible_text('Morning')

# Select by index
#dropdown_box.select_by_index(2) # Afternoon

# Select by Value
dropdown_box.select_by_value('Radio-2') # Evening

# Count number of Options
all_options = dropdown_box.options
print(f'Number of options available: {len(all_options)}')

# Capture all the options and print them as output
for option in all_options:
    print(option.text)