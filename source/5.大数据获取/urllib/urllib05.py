from urllib.parse import urlparse
o = urlparse(' http://www.nwpu.edu.cn/xysz.htm ')
print(o)
print(o.scheme)
print(o.port)
print(o.geturl)
