import re
content = '''
<td>
<a href="http://www.nwpu.edu.cn/">西北工业大学</a>
<a href="https://jsj.nwpu.edu.cn/">西北工业大学计算机学院</a>
</td>
'''
# 获取<a href></a>之间的内容
result_pattern = r'<a .*?>(.*?)</a>'
results = re.findall(result_pattern, content, re.S|re.M)
for result in results:
    print(result)

# 获取所有<a href></a>之间的url
url_pattern = r'href="(.*?)"'
urls = re.findall(url_pattern, content, re.I|re.S|re.M)
for url in urls:
    print(url)
