from spyUtils import spyUtils
from datetime import datetime

class mainSpy:

    def main(self):
        page = spyUtils.get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
        if page:
            time = datetime.today()
            date = time.strftime("%m/%d").lstrip('0')  # 今天日期, 去掉開頭的 '0' 以符合 PTT 網站格式
            current_articles = spyUtils.get_articles(page, date)
            for article in current_articles:
                # print(article)
                PTT_URL = 'https://www.ptt.cc'
                page = spyUtils.get_web_page(PTT_URL+article['href'])
                if page:
                    # spyUtils.get_push(page)
                    img_urls = spyUtils.parse(page)
                    spyUtils.save(img_urls,article['title'])
                    article['num_image'] = len(img_urls)
                    # with open('data.json', 'w', encoding='utf-8') as f:
                    # json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)
            

mainSpy =  mainSpy()
mainSpy.main()