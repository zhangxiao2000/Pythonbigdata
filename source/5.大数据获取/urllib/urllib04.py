from urllib import request, error
try:
    response = request.urlopen("http://www.nwpu.edu.cn/xyszhtm")
except error.HTTPError as ex:
    print(ex.reason, ex.code, ex.headers, sep="\n")
