import requests

# 使用post方式
data = {"name": "zx","school":"nwpu"}
r = requests.post('http://httpbin.org/post', data = data)
print(r.text)

# 使用字典形式传入参数
data = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)

# 使用元组列表形式传入参数
data = (('key1', 'value1'), ('key1', 'value2'))
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)


