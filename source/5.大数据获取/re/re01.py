import re

# match函数使用
print(re.match('www', 'www.nwpu.edu.cn/').span())  # 在起始位置匹配
print(re.match('cn', 'www.nwpu.edu.cn/'))

# search函数的确使用
print(re.search('www', 'www.nwpu.edu.cn').span())  # 在起始位置匹配
print(re.search('cn', 'www.nwpu.edu.cn').span())         # 不在起始位置匹配

# sub函数使用
phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)

# compile函数使用
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)


# finditer函数使用
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group())

# findall函数使用
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
