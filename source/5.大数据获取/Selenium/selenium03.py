from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.baidu.com')
print(driver.find_element_by_css_selector('#kw'))
print(driver.find_element_by_xpath('//*[@id="kw"]'))
driver.close()

