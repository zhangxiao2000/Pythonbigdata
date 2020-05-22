import requests

# 不添加请求头
r = requests.get("https://www.zhihu.com/explore")
print(r.text)


# 添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
print(r.text)

r = requests.get(' https://www.zhihu.com/explore ')
print(r.headers)
print(r.headers["content-type"])