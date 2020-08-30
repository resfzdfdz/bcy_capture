import requests
import json
import os
import re
import time

import warnings
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

tag = '初音ミク 50000users入り'

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"

pixiv_cookie = 'first_visit_datetime_pc=2018-09-02+20%3A23%3A12; p_ab_id=1; p_ab_id_2=8; _ga=GA1.2.692557459.1535887398; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=17487266=1^9=p_ab_id=1=1^10=p_ab_id_2=8=1^11=lang=zh=1; ki_r=; p_ab_d_id=1442639323; yuid_b=JgCVBIE; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; privacy_policy_agreement=1; adr_id=5HYdqWgBaFqfwCZd3P2l7z1axyzT2gnpp6yI16s1nca5eUYj; c_type=23; ki_u=9a8b9143-e6cf-fcfb-9001-90c8; __gads=ID=ad7362c3ed8ae9ad:T=1565164699:S=ALNI_MZf5-8MJ8ATuZZoEDzYxOEGqxzWTA; __utmz=235335808.1571062237.197.3.utmcsr=saucenao.com|utmccn=(referral)|utmcmd=referral|utmcct=/search.php; _td=53981b0b-e333-4ee7-805a-ca15059d3758; categorized_tags=4DIu_dD_V7~G6EmdndVFn~H1p_1O8iE9~HxenCaC-zZ~JtHr1OyMVc~K0rq4tmPAD~M1EbAsbWwh~OT4SuGenFI~TnBACGj8Pf~YKAliF34Ha~fgp2llLuiV~kP7msdIeEU~qovLKmp6Fx~uG0wcfxlfN~wENnjb8dn3~x_ZoCoDo92~yBnMz57lw_; is_sensei_service_user=1; tags_sended=1; OX_plg=pm; __utma=235335808.692557459.1535887398.1576676758.1576936390.246; __utmc=235335808; _gid=GA1.2.42292165.1576937308; ki_s=197685%3A0.0.0.0.0%3B198264%3A1.1.0.1.1%3B198890%3A0.0.0.0.0%3B199710%3A0.0.0.0.0%3B200349%3A0.0.0.0.0%3B201056%3A0.0.0.0.0%3B201971%3A0.0.0.0.0%3B202660%3A0.0.0.0.0; tag_view_ranking=OT4SuGenFI~kP7msdIeEU~K0rq4tmPAD~Lt-oEicbBr~G6EmdndVFn~_Ed3oLjsrz~jaqkarpwly~8KW7VaZU1P~HK8fptdyiI~eVxus64GZU~JtHr1OyMVc~rYZfDSxU_2~YKAliF34Ha~4Ew9pzGr3u~3mLXnunyNA~NgHIkiGFP2~wqBB0CzEFh~w8ffkPoJ_S~yBnMz57lw_~Zt2G8E4LoU~qshHNrlqER~B_xRqScMCg~0gj7UYa-6O~uW5495Nhg-~kBTdxTbN_P~BF8N0C5-64~KMpT0re7Sq~bPI9qoWvsg~Nh8v-uMkzm~QwQ3wReUTs~uG0wcfxlfN~fgp2llLuiV~Itu6dbmwxu~4DIu_dD_V7~FZHZZbK5iC~wENnjb8dn3~XoXIjxuZvN~S0eWMRWoH6~PwDMGzD6xn~vFXX3OXCCb~wmxKAirQ_H~d73AdVrO-6~MisUG1fO4l~-AW_uJQ9pz~KvAGITxIxH~RokSaRBUGr~zamoiem15e~q303ip6Ui5~1n2KtPTBC_~sLNtd-JQXp~ux8ydyywfL~ig3dmVOeR7~Ed_W9RQRe_~pzzjRSV6ZO~M1EbAsbWwh~rwd-dOT_5b~nV8SCejtDp~OACN2BwvTX~6C33Od2MhM~jlaWO04msk~0uAsWI2pj3~8EujxjXTAc~s0TsWWEX5f~HxenCaC-zZ~-W2Dedn37P~Ln_RqH3kDI~Cr3jSW1VoH~VT5sJnSWvI~mqf4KYn6Dx~EaExj72YKy~pbqmgYwTBU~8XX2eqWqNX~0xsDLqCEW6~0CaTbfGZYk~42WYuu40N2~BQFWWhxtER~1lj4xMFGha~Rh_E4IFhDH~x_ZoCoDo92~qovLKmp6Fx~VQqg_4GSt0~vYhajYKZ7I~PJYNjPi7CI~JN2fNJ_Ue2~ZXFMxANDG_~lxfrUKMf9f~AoKfsFwwdu~TnBACGj8Pf~RKAHEY3QDd~1F9SMtTyiX~ht-sf3LJGn~yt_SIzY_dF~gFv6cfMyax~ySlbl0E5DF~LowUF3jomy~bZ-pSZkRdg~BOtYmZ06Vx~jhuUT0OJva~_hSAdpN9rx~H2bcNQ0hvl; __utmt=1; ki_t=1536040894402%3B1576937375751%3B1576940344227%3B102%3B153; PHPSESSID=q80c2a6mdjqg1m3s8rb0d23qf8iu06fv; login_bc=1; __utmb=235335808.39.9.1576940341488\'first_visit_datetime_pc=2018-09-02+20%3A23%3A12; p_ab_id=1; p_ab_id_2=8; _ga=GA1.2.692557459.1535887398; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=17487266=1^9=p_ab_id=1=1^10=p_ab_id_2=8=1^11=lang=zh=1; ki_r=; p_ab_d_id=1442639323; yuid_b=JgCVBIE; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; privacy_policy_agreement=1; adr_id=5HYdqWgBaFqfwCZd3P2l7z1axyzT2gnpp6yI16s1nca5eUYj; c_type=23; ki_u=9a8b9143-e6cf-fcfb-9001-90c8; __gads=ID=ad7362c3ed8ae9ad:T=1565164699:S=ALNI_MZf5-8MJ8ATuZZoEDzYxOEGqxzWTA; __utmz=235335808.1571062237.197.3.utmcsr=saucenao.com|utmccn=(referral)|utmcmd=referral|utmcct=/search.php; _td=53981b0b-e333-4ee7-805a-ca15059d3758; categorized_tags=4DIu_dD_V7~G6EmdndVFn~H1p_1O8iE9~HxenCaC-zZ~JtHr1OyMVc~K0rq4tmPAD~M1EbAsbWwh~OT4SuGenFI~TnBACGj8Pf~YKAliF34Ha~fgp2llLuiV~kP7msdIeEU~qovLKmp6Fx~uG0wcfxlfN~wENnjb8dn3~x_ZoCoDo92~yBnMz57lw_; is_sensei_service_user=1; tags_sended=1; OX_plg=pm; __utma=235335808.692557459.1535887398.1576676758.1576936390.246; __utmc=235335808; _gid=GA1.2.42292165.1576937308; ki_s=197685%3A0.0.0.0.0%3B198264%3A1.1.0.1.1%3B198890%3A0.0.0.0.0%3B199710%3A0.0.0.0.0%3B200349%3A0.0.0.0.0%3B201056%3A0.0.0.0.0%3B201971%3A0.0.0.0.0%3B202660%3A0.0.0.0.0; tag_view_ranking=OT4SuGenFI~kP7msdIeEU~K0rq4tmPAD~Lt-oEicbBr~G6EmdndVFn~_Ed3oLjsrz~jaqkarpwly~8KW7VaZU1P~HK8fptdyiI~eVxus64GZU~JtHr1OyMVc~rYZfDSxU_2~YKAliF34Ha~4Ew9pzGr3u~3mLXnunyNA~NgHIkiGFP2~wqBB0CzEFh~w8ffkPoJ_S~yBnMz57lw_~Zt2G8E4LoU~qshHNrlqER~B_xRqScMCg~0gj7UYa-6O~uW5495Nhg-~kBTdxTbN_P~BF8N0C5-64~KMpT0re7Sq~bPI9qoWvsg~Nh8v-uMkzm~QwQ3wReUTs~uG0wcfxlfN~fgp2llLuiV~Itu6dbmwxu~4DIu_dD_V7~FZHZZbK5iC~wENnjb8dn3~XoXIjxuZvN~S0eWMRWoH6~PwDMGzD6xn~vFXX3OXCCb~wmxKAirQ_H~d73AdVrO-6~MisUG1fO4l~-AW_uJQ9pz~KvAGITxIxH~RokSaRBUGr~zamoiem15e~q303ip6Ui5~1n2KtPTBC_~sLNtd-JQXp~ux8ydyywfL~ig3dmVOeR7~Ed_W9RQRe_~pzzjRSV6ZO~M1EbAsbWwh~rwd-dOT_5b~nV8SCejtDp~OACN2BwvTX~6C33Od2MhM~jlaWO04msk~0uAsWI2pj3~8EujxjXTAc~s0TsWWEX5f~HxenCaC-zZ~-W2Dedn37P~Ln_RqH3kDI~Cr3jSW1VoH~VT5sJnSWvI~mqf4KYn6Dx~EaExj72YKy~pbqmgYwTBU~8XX2eqWqNX~0xsDLqCEW6~0CaTbfGZYk~42WYuu40N2~BQFWWhxtER~1lj4xMFGha~Rh_E4IFhDH~x_ZoCoDo92~qovLKmp6Fx~VQqg_4GSt0~vYhajYKZ7I~PJYNjPi7CI~JN2fNJ_Ue2~ZXFMxANDG_~lxfrUKMf9f~AoKfsFwwdu~TnBACGj8Pf~RKAHEY3QDd~1F9SMtTyiX~ht-sf3LJGn~yt_SIzY_dF~gFv6cfMyax~ySlbl0E5DF~LowUF3jomy~bZ-pSZkRdg~BOtYmZ06Vx~jhuUT0OJva~_hSAdpN9rx~H2bcNQ0hvl; __utmt=1; ki_t=1536040894402%3B1576937375751%3B1576940344227%3B102%3B153; PHPSESSID=q80c2a6mdjqg1m3s8rb0d23qf8iu06fv; login_bc=1; __utmb=235335808.39.9.1576940341488'

base_url = 'https://www.pixiv.net'

user_head={     
    'Accept': "application/json", 
    'Accept-Encoding': "gzip, deflate, sdch, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cache-Control':'max-age=0',
    "Connection": "keep-alive",
##    'Cookie' : pixiv_cookie,
    'Referer' : base_url,
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': agent    
}

login_url = 'https://accounts.pixiv.net/login?lang=zh'

def login(): #登录
	#模拟一下浏览器
    head={   
	    'User-Agent': agent,
	    'Referer':'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=64503210',
            'cookie' : pixiv_cookie
	    }
	    
	#用requests的session模块记录登录的cookie
    session = requests.Session()

	#首先进入登录页获取post_key，我用的是正则表达式
    response = session.get(login_url, verify = False)  
    post_key = re.findall('<input type="hidden" name="post_key" value=".*?">',
                          response.text)[0]
    post_key = re.findall('value=".*?"',post_key)[0]
    post_key = re.sub('value="','',post_key)
    post_key = re.sub('"', '',post_key)
##    print(post_key)
    
    #将传入的参数用字典的形式表示出来，return_to可以去掉
    data = {
        'pixiv_id': "1040470561",
        'password': "hpf123456",
        'captcha':  "",
        'get_recaptcha_response':   "",
        'post_key': post_key,
        'source':   "accounts",
        "ref":      "",
        'return_to': 'https://www.pixiv.net/',
    }
    
    #将data post给登录页面，完成登录
    a = session.post(login_url, data=data, headers=head, verify = False)

    with open('login.txt', 'wb') as fp:
        fp.write(a.content)
        fp.flush()
        
    return session

##########################
def get_pixiv_url(session, from_page, des_page):
    start = time.time()
    url_id = []
    for page in range(from_page, des_page+1):
        search_url = 'https://www.pixiv.net/ajax/search/artworks/{p_tag}?word={p_tag}&order=date_d&mode=all&p={p_page}&s_mode=s_tag&type=all'.format(p_tag = tag, p_page = page)
##        search_url = 'https://www.pixiv.net/ajax/search/illustrations/\
##		{p_tag}?word={p_tag}&order=date_d&mode=all&p={p_page}&s_mode=\
##		s_tag_full&type=illust_and_ugoira'.format(p_tag = tag, p_page = page)
        req = session.get(search_url, verify = False )

        js_str = req.text
        dic_str = json.loads(js_str)
        illust_data = dic_str["body"]["illustManga"]["data"]
##        illust_data = dic_str["body"]["illust"]["data"]

        url_head = 'https://www.pixiv.net/artworks/'

        for per in illust_data:
            if ('illustId' in per):
                url_id.append(url_head + per["illustId"])
            
    print('get url_id done!')
    finish = time.time()
    print('elapsed time = ', finish - start, 's\n')
    
    return url_id

def favor_sieve(session, url_id, min_favor):
    start = time.time()
    image_url = []
    for per in url_id:
        try:
            r = session.get(per, headers = user_head, verify = False)

            text = r.text
            s = text.split('\n')
            for hp in s:
                if '</script>' in hp:
                    t = hp

    ##  爬取赞数likeCount
            w = t.split("likeCount")
            z = re.findall('\d+', w[1])
            likeCount = int(z[0])
##            print('likeCount = ', likeCount)
##            print('url = ', per)

            if (likeCount < min_favor):
                continue
            else:
    ##  爬取原图url
                x = t.split('"original"')
                y = x[1].split('"')
                original = y[1]

                image_url.append(original)
        except:
            continue

    finish = time.time()
    print('favor sieve done!')
    print('{num} collected!'.format(a = len(image_url)))
    print('elapsed time = ', finish - start, 's\n')
    return image_url

def download_one(session, url, timeout):
    start = time.time()
    res = session.get(url, stream = True, headers = user_head, \
                       verify = False, timeout = timeout)

    s = url.split('/')
    name = './image/' + tag + ' ' + s[-1]

    with open(name, 'wb', buffering = 512 * 1024) as fp:
        fp.write(res.content)
        fp.flush()
        
    finish = time.time()
    print('finish download {u}!'.format(u = s[-1]) )
    print('elapsed time = ', finish - start, 's\n')

def download_pixiv(session, image_url):
    start = time.time()
    timeout = 5
    total_url = image_url
    while(1):
        timeout_url = []
        for per in total_url:
            try:
                download_one(session, per, timeout)
            except:
                timeout_url.append(per)
        total_url = timeout_url
        timeout += 10
        if ( (timeout_url == []) or (timeout > 200) ):
            break

    finish = time.time()
    print('total elapsed time = ', finish - start, 's\n')

##if __name__ == '__main__':
##    s = login()
##    url_id = get_pixiv_url(s, 25, 25)

if __name__ == '__main__':
    s = login()
    url_id = get_pixiv_url(s, 1, 4)
    image_url = favor_sieve(s, url_id, 0)
    download_pixiv(s, image_url)

