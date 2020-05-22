#encoding=utf-8
from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">西北工业大学</b>','lxml')

# BeautifulSoup属性
print(type(soup))
print(soup.name)

# tag属性
tag = soup.b
print(type(tag))
print(tag.name)

# 修改name
tag.name = "p"
print(tag)
print(tag.attrs)

# 获取class属性的值
print(tag["class"])
# 修改class属性的值
tag["class"] = "nwpu"
# 增加一个id属性
tag["id"] = "1"
print(tag)
# 删除id属性
del tag['id']
print(tag)

# NavigableString属性
print(tag.string)
print(type(tag.string))

#  replace_with() 的使用
tag.string.replace_with("西北工业大学计算机学院")
print(tag)


# comment属性
markup = "<b><!--I am a student of NWPU--></b>"
soup = BeautifulSoup(markup,'lxml')
comment = soup.b.string
print(type(comment))
print(comment)
