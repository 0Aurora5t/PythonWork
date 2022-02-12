'''导入urllib库的URLopen'''
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as bf
'''
#发出请求，获取HTML
html=urlopen("http://www.baidu.com/")
#获取的HTML内容是字节，将其转化为字符串
html_text=bytes.decode(html.read())
print(html_text)
'''
#请求获取HTML
html=urlopen("http://www.baidu.com/")
#使用BeautifulSoup解析HTML
obj=bf(html.read(),'html.parser')
#从标签head、title里提取标题
title=obj.head.title
#使用find_all函数获取所有图片信息
pic_info=obj.find_all('img',class_="index-logo-src")
#只提取logo图片的链接
logo_url="https:"+pic_info[0]['src']
#使用urlretrieve下载图片
urlretrieve(logo_url,'logo.png')
print(logo_url)
'''#分别打印每张图片的信息
for i in pic_info:
    print(i)
print(title)'''
