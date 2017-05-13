#Run in python3.5, use python3.5 ptt_crawlet.py to run
#Crawler for ptt

import requests
import time
#from bs4 import BeautifulSoup

#func
def get_web_page(url):
    time.sleep(0.5)  # 每次爬取前暫停 0.5 秒以免被 PTT 網站判定為大量惡意爬取
    resp = requests.get(
        url=url,
        cookies={'over18': '1'},
        verify=False
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp


#main
if __name__ == '__main__':
    res = get_web_page("https://www.ptt.cc/bbs/Hsinchu/index1.html")
    #res = requests.get("https://www.ptt.cc/bbs/Hsinchu/index1.html",verify=False)
    #res = requests.get("https://www.ptt.cc/bbs/Hsinchu/index.html",cookies={'over18': '1'},verify=False)
    print(res.text)



