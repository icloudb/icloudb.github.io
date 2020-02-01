import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--save-page-as-mhtml')

browser = webdriver.Chrome(options=chrome_options)
browser.set_window_size(1024, 768) # optional
browser.set_page_load_timeout(15)
browser.get('https://free-ss.site')
time.sleep(5) #等待
browser.save_screenshot('./_site/ss.png') # save a screenshot to disk
html_source = browser.page_source
browser.close()

file = open('./_site/ss.html','w')
file.write(html_source)
file.close()
