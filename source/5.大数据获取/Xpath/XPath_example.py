from lxml import etree

# 读取html内容
html = etree.parse(r"../data/Xpathexample.html", etree.HTMLParser())
result = etree.tostring(html)
print(result.decode("utf-8"))

# 获取所有节点
allnodes = html.xpath("//*")
print(allnodes)

# 获取指定节点
all_p = html.xpath("//p")
print(all_p)

# 获取子节点
child_a = html.xpath("//p/a")
print(child_a)

# 获取父节点
parent_node = html.xpath('//a[@href="http://www.nwpu.edu.cn"]//../@class')
print(parent_node)

# 获取节点文本信息
content = html.xpath('//p/a[@href="http://www.nwpu.edu.cn"]/text()')
print(content)

# 获取超链接
urls = html.xpath("//p/a/@href")
print(urls)


