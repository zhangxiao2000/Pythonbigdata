import requests

# 二进制响应内容
r = requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)


from PIL import Image
from io import BytesIO
im = Image.open(BytesIO(r.content))
im.show() # 显示图片
im.save("test.png") # 保存图片
