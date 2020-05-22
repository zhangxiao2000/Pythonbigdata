from urllib import request, error
try:
    response = request.urlopen("http://www.nwpu.edu.cn/index.html")
except error.URLError as ex:
    print(ex.reason)


try:
    response = request.urlopen("http://www.nwpu.edu.com")
    print(response.status)
    print(response.read())
except error.URLError as ex:
    print(ex.reason)
