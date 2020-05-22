from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.douban.com/')
icp = driver.find_element_by_id('icp')
print(icp)
## 获取节点class属性
print(icp.get_attribute('class'))
## 获取文本内容
print(icp.text)
driver.close()