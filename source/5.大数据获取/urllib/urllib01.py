import urllib.request

# 使用urlopen
response=urllib.request.urlopen("http://www.nwpu.edu.cn")
print(response.read().decode("utf-8"))

# 查看response类型
print(type(response))

# 查看response的一些属性
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
