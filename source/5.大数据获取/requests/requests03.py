import requests

# 传递url参数
params = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=params)
print(r.url)

# 将参数以列表形式传入
data = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=data)
print(r.url)

