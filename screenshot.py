'''
This program takes a screen shot of the full webpage
'''

from selenium import webdriver
import time

# Chrome
browser_driver_location = '/home/theo/Workspace/browsersDriver/chromedriver'
browser = webdriver.Chrome(executable_path=browser_driver_location)
url = r'https://python.org'
browser.get(url)
time.sleep(2)

download_path = '/home/theo/Downloads/Test/'

try:
    browser.get_screenshot_as_file(f'{download_path}screenshot.png')
    browser.close()
except:
    print(f"Something went wrong!")

print('end..')