#encoding=utf-8
from bs4 import BeautifulSoup
from lxml import etree
import re
html = etree.parse(r"..\data\豆瓣电影排行榜.html", etree.HTMLParser())
html = etree.tostring(html).decode("utf-8")
soup = BeautifulSoup(html, 'lxml')
# 获取所有电影
films = soup.find_all(name='div', class_='pl2')
# 获取所有的电影名称和评分,将结果保存在一个字典中
result = {}
#  遍历films列表，其中的每一个元素都是一个Tag对象
for film in films:
    # 将获取到的迭代器转化为list，并将list中的第一个元素转化为字符串形式
    string = str(list(film.find('a', class_='').children)[0])
    # 利用正则表达式将string中的电影名提取出来
    film_name = re.sub(r'[\r\n\s/]*', ' ',  string)
    # 获取电影评分
    star_div = film.find(name='div', class_='star clearfix')
    star_num_div = film.find(name='div', class_='star clearfix')
    star_num = star_num_div.find(name='span', class_='rating_nums').string
    result[film_name] = float(str(star_num))
print(result)