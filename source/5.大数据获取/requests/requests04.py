import requests

r = requests.get('http://www.nwpu.edu.cn')
# 设置编码格式，防止中文乱码
r.encoding = "UTF-8"
print(r.text)

print(r.encoding)
