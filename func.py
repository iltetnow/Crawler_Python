import requests
import time
from bs4 import BeautifulSoup

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
        return BeautifulSoup(resp.text, "html.parser")

def search_result(soup, SearchKW, PttURL, PttLinkTag):
    for entry in soup.select('.r-ent'):
        if SearchKW in entry.select('.title')[0].text: 
            print(entry.select('.title')[0].text)
            print("Date: "+entry.select('.date')[0].text, ", Author: "+entry.select('.author')[0].text)
            for linktag in entry.findAll('a',href=True):
                if linktag.get('href').startswith(PttLinkTag): 
                    print(PttURL+linktag.get('href'))
            print("----------------------------------------------------------")
