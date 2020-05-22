# 获取百度源码
# 初始化selenium并导入selenium库
from selenium import webdriver
# 使用相对路径指定WebDriver
driver = webdriver.Chrome('chromedriver.exe')
try:
    # 使用selenium打开网页
    driver.get('https://www.baidu.com')
    # 获取网页源代码
    html = driver.page_source
    print(html) # 打印网页源代码
finally:
    driver.close()
