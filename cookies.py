from selenium import webdriver
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
browser = webdriver.Chrome(executable_path=browser_driver_location)

url = r'https://www.google.com'

browser.get(url)
cookies = browser.get_cookies()

# iterate through the cookies
for cookie in cookies:
    print(f'Cookie: {cookie}')

browser.delete_all_cookies()
print(f'Cookies after deleting: {browser.get_cookies()}')
browser.close()