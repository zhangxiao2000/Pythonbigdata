from urllib.parse import urlunsplit
data = ["http", " www.nwpu.edu.cn ", "index.html", "a=7", "comment"]
print(urlunsplit(data))
