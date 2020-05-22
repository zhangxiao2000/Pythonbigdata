from selenium import webdriver
# 使用相对路径指定WebDriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.baidu.com')
element_by_name= driver.find_element_by_name('wd')
element_by_id = driver.find_element_by_id('kw')
print(element_by_name)
print(element_by_id)
driver.close()
