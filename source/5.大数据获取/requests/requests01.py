import requests

# 发送请求
r = requests.get("https://www.nwpu.edu.com")
print(type(r))
print(r.status_code)
print(r.cookies)


