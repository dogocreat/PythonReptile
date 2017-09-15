import requests
import urllib.request
import json,re
import os, sys
from bs4 import BeautifulSoup

class spyUtils:
    
    def __init__(self):
        super(spyUtils, self).__init__()

    def get_web_page(url):
        resp = requests.get(
            url=url,
            cookies={'over18': '1'}
        )
        if resp.status_code != 200:
            print('Invalid url:', resp.url)
            return None
        else:
            return resp.text

    def get_articles(dom, date):
        soup = BeautifulSoup(dom, 'html.parser')
        articles = []  # 儲存取得的文章資料
        divs = soup.find_all('div', 'r-ent')
        for d in divs:
            if d.find('div', 'date').string.strip() == date:  # 發文日期正確 需轉換前後空白 .strip()
                # 取得推文數
                push_count = 0
                if d.find('div', 'nrec').string:
                    try:
                        push_count = int(d.find('div', 'nrec').string)  # 轉換字串為數字
                    except ValueError:  # 若轉換失敗，不做任何事，push_count 保持為 0
                        pass

                # 取得文章連結及標題			
                if d.find('a'):  # 有超連結，表示文章存在，未被刪除
                    href = d.find('a')['href']
                    title = d.find('a').string
                    articles.append({
                        'title': title,
                        'href': href,
                        'push_count': push_count
                    })
        return articles

    def parse(dom):
        soup = BeautifulSoup(dom, 'html.parser')
        links = soup.find(id='main-content').find_all('a')
        img_urls = []
        for link in links:
            if re.match(r'^https?://(i.)?(m.)?imgur.com', link['href']):
                img_urls.append(link['href'])
        return img_urls

    def save(img_urls, title):
        if img_urls:
            try:
                dname = title.strip()  # 用 strip() 去除字串前後的空白
                os.makedirs(dname)
                for img_url in img_urls:
                    if img_url.split('//')[1].startswith('m.'):
                        img_url = img_url.replace('//m.', '//i.')
                    if not img_url.split('//')[1].startswith('i.'):
                        img_url = img_url.split('//')[0] + '//i.' + img_url.split('//')[1]
                    if not img_url.endswith('.jpg'):
                        img_url += '.jpg'
                    fname = img_url.split('/')[-1]
                    urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
            except Exception as e:
                print(e)

    def get_push(dom):
        soup = BeautifulSoup(dom, 'html.parser')
        pushs = soup.find_all('div','push')
        push_arr = []  
        for push in pushs:
            if push.find('span','f3 push-content'):
                # print(push.find('span','f3 push-content').string)
                push_userid = push.find('span','f3 hl push-userid').string
                push_msg = push.find('span','f3 push-content').string
                push_arr.append({
                    'userid': push_userid,
                    'msg': push_msg,
                })

        # print(push_arr)
        # with open('push_msg.json', 'a', encoding='utf-8') as f:
        #     json.dump(push_arr, f, ensure_ascii=False)
        # with open('push_msg.json', 'r', encoding='utf-8') as r:
        #     content = r.readline();
        #     print(content.encode('utf-8').decode('utf-8'))