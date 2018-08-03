# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:14:44 2018

@author: yennefer
"""

#%%
import requests
#r = requests.get('http://www.baidu.com')#使用get方法打开百度链接
r.encoding = 'utf-8'
#%%
import requests
def getHTMLText(obj):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发异常
        r.encoding = 'utf-8'#无论原来用什么编码，都改成utf-8
        return r.text
    except:
        return ""
url = "http://www.baidu.com"
print(getHTMLText(url))
#%%
import requests
from bs4 import BeautifulSoup
r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text)
print(soup.p)
#%%
from urllib import request
import chardet
if __name__ == '__main__':
    response = request.urlopen('http://fanyi.baidu.com')
    html = response.read()
    chardet = chardet.detect(html)
    print(chardet)# 查看编码方式
    html = html.decode('utf-8')#解码，显示出来
    print(html) #简单的网页读取
    #%%
from urllib import request
if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/") #定义Request的对象
    response = request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    print(html)
#%%
from urllib import request

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print("geturl打印信息：%s"%(response.geturl()))#返回的是一个url的字符串
    print('**********************************************')
    print("info打印信息：%s"%(response.info()))#返回的是一些meta标记的元信息，包括一些服务器的信息
    print('**********************************************')
    print("getcode打印信息：%s"%(response.getcode()))#返回的是HTTP的状态码，如果返回200表示请求成功

    



