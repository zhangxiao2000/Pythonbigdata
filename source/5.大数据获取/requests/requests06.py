import requests

# json响应内容
r = requests.get('https://api.github.com/events')
print(r.json())

# json解码失败
r = requests.get('http://www.nwpu.edu.cn')
print(r.json())

