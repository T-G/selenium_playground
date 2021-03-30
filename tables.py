from selenium import webdriver
from selenium.webdriver.common.by import By

browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'

driver = webdriver.Chrome(executable_path=browser_driver_location)

url = r'http://www.dhs.state.il.us/accessibility/tests/simple-table-test.html'

driver.get(url)

# Finding the number of Rows
no_of_rows = len(driver.find_elements_by_xpath('/html/body/main/table[2]/tbody/tr'))
print(f'No. of rows: {no_of_rows} ')

# Finding the number of Columns
no_of_cols = len(driver.find_elements_by_xpath('/html/body/main/table[2]/thead/tr/th'))
print(f'No. of cols: {no_of_cols}')

#/html/body/main/table[1]/tbody/tr[1]/td[1]
# Extracting the data from the html table
print(f'Name     \tAge Sex \tRace')
print(f'---------\t--- --- \t----')
for row in range(1 , no_of_rows + 1):
    for col in range(1 , no_of_cols + 1):
        data = driver.find_element_by_xpath(f'/html/body/main/table[2]/tbody/tr[{str(row)}]/td[{str(col)}]').text
        print(data, end='\t')
    print()
