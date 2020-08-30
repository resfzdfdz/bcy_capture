import requests
import json
import os
import time
from bs4 import BeautifulSoup

##url = 'https://bcy.net/item/detail/6423813912671575822?_source_page='
##url = 'https://bcy.net/item/detail/6433062149785935630?_source_page='
##url = 'https://bcy.net/item/detail/6568766941534617863?_source_page='
##url = 'https://bcy.net/item/detail/6409190270583201550?_source_page='
##url = 'https://bcy.net/item/detail/6331707235202260750?_source_page='
##url = 'https://bcy.net/item/detail/6793270733666524164'
##url = 'https://bcy.net/item/detail/6807760509161439500'
##url = 'https://bcy.net/item/detail/6807325390210604036'
##url = 'https://bcy.net/item/detail/6809219702569566472'
##url = 'https://bcy.net/item/detail/6827483117666704397'
##url = 'https://bcy.net/item/detail/6829180854187596803'
##url = 'https://bcy.net/item/detail/6735936029242432515'
##url = 'https://bcy.net/item/detail/6793325791082978307'
##url = 'https://bcy.net/item/detail/6795786285643471880'
url = 'https://bcy.net/item/detail/6795822627307913479'

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

image_urls = []

req2 = requests.get(url, headers = user_head)
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

print('URL Parsed Done!', len(image_urls), 'Object Found\n')

num = 0
lo_musume = '分解因式'
lolita_dress = ' 花嫁'
for per in image_urls:
    start = time.time()
    fname = './image/' + lo_musume + lolita_dress + str(num) + '.jpg'
    pic = requests.get(per, stream = True, headers = user_head)
    with open(fname, 'wb', buffering = 1024*1024) as fp:
        fp.write(pic.content)
        fp.flush()
    num += 1
    finish = time.time()
    duration = (finish - start)
    print ('OBJ {inum} Download!'.format(inum = num - 1))
    print ('Elapsed Time = {dur} s\n'.format(dur = duration))
