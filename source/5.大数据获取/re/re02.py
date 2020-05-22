import re

content = '''<tr><th>西北工业大学</th><td>计算机学院</td></tr>'''
# 获取tr中的内容
pattern_tr = r"<tr>(.*?)</tr>"
content_tr = re.findall(pattern_tr, content, re.S | re.M)
for tr in content_tr:
    print(tr)

# 获取th中的内容
pattern_th = r"<th>(.*?)</th>"
content_th = re.findall(pattern_th, tr, re.S | re.M)
for th in content_th:
    print(th)

# 获取td中的内容
pattern_td = r"<td>(.*?)</td>"
content_td = re.findall(pattern_td, tr, re.S | re.M)
for td in content_td:
    print(td)
