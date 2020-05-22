from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.douban.com/')
print(driver.find_elements_by_css_selector('.anony-nav-links li'))
driver.close()
