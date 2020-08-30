import requests
import json
import os
from bs4 import BeautifulSoup

web_url = "https://bcy.net"
search = '洛天依'

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

user_head={     
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    'Accept-Encoding': "gzip, deflate, sdch, br",
    'Accept-Language': "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2",
    'Cache-Control':'max-age=0',
    "Connection": "keep-alive",
    'Referer': 'https://bcy.net/start',
    'User-Agent': agent    
}

req = requests.get("https://bcy.net/search/home?k={stype}"\
                   .format(stype = search), headers = user_head)
text = req.content
soup = BeautifulSoup(text, 'lxml')

urls = []

lists = soup.find_all('li', class_ = 'js-smallCards _box')
for per_list in lists:
    v = per_list.a
    urls.append( v['href'] )

image_urls = []
for per in urls:
##    per = '/item/detail/6671262800045670669'
    real_url = web_url + per
    req2 = requests.get(real_url, headers = user_head)
    text2 = req2.content
    soup2 = BeautifulSoup(text2, 'lxml')
    body = soup2.body
    s1 = body.script
    a = str(s1)
    b = a.split('\"origin\\\"')
    for mb in b[1:]:
        b1 = mb.split('\"')
        b2 = b1[1].replace('\\\\u002F', '/')
        image_urls.append( b2[:-1] )

##num = 0
##max_num = 20
##for per in image_urls[:max_num]:
##    fname = './image/' + str(num) + '.jpg'
##    pic = requests.get(per, stream = True, headers = user_head)
##    with open(fname, 'wb', buffering = 4*1024) as fp:
##        fp.write(pic.content)
##        fp.flush()
##    num += 1
    
