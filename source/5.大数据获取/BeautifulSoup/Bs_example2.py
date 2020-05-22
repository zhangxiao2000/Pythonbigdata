#encoding=utf-8
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_doc,"lxml")

# contents和children
head_tag = soup.head
print(head_tag)
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

for child in title_tag.children:
    print(child)

# descendants
print(type(head_tag.descendants))
for child in head_tag.descendants:
    print(child)


# parent
print(title_tag.parent)
# BeautifulSoup对象的parent属性是None。
html_tag = soup.html
print(type(html_tag.parent))
print(soup.parent)

# parents：遍历<a>便签到根节点的所有节点。
link = soup.a
print(link)
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

# next_sibling和previous_sibling
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>","lxml")
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

print(sibling_soup.b.previous_sibling)
print(sibling_soup.c.next_sibling)

# next_siblings和previous_siblings
for sibling in soup.a.next_siblings:
    print(repr(sibling))
for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))


# find_all()函数使用
# 传入name属性
print(soup.find_all(name='a'))

# 传入attrs属性
print(soup.find_all(attrs={'class','sister'}))

# 传入recursive属性
# 在所有子节点中查找名为title的所有子节点
print(soup.find_all("title"))
# 在所有直接子节点中查找名为title的所有子节点
print(soup.html.find_all("title", recursive=False))

# 传入text属性
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))

# 子节点内容与其父节点内容一致
def is_the_only_string_within_a_tag(s):
    return (s == s.parent.string)
print(soup.find_all(text=is_the_only_string_within_a_tag))


# find()函数的使用
print(soup.find('p'))
print(type(soup.find('p')))

# 在find_all()函数中使用limit参数
print(soup.find_all('p', limit=1))

# 比较二者对空值的处理
print(soup.find("NWPU"))
print(soup.find_all("NWPU"))








