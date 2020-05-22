from urllib.parse import urlunparse
data = ["http", "www.nwpu.edu.cn", "index.html", "user", "a=7", "comment"]
print(urlunparse(data))
