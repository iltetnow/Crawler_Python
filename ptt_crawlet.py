#Run in python3.5, use python3.5 ptt_crawlet.py to run
#Crawler for ptt
from func import *
import sys
import datetime

#global variable
WebURLBase = "https://www.ptt.cc/bbs"
WebURLEnd = "index.html"
PttURL = "https://www.ptt.cc"
UpPageKW = "上頁"
PttLinkTag = "/bbs"

SearchBoard = "Hsinchu"
SearchKW = "贈送"
SearchPageRange = 3
#SearchDate = datetime.date.today()

#main
if __name__ == '__main__':
    #Process the input parameter
    InLength = len(sys.argv)

    if InLength >= 2:
        if sys.argv[1] == "-h":
            print("Usage: python3.5 ptt_crawlet.py [SearchBoard] [SearchKW] [SearchPageRange]")
        elif InLength == 4:
            SearchBoard = sys.argv[1]
            SearchKW = sys.argv[2]
            SearchPageRange = int(sys.argv[3])
        else:
            print("Wrong input parameter, run the default parameter: Hsinchu 贈送 10")
            
    print("----------------------------------------------------------")
    WebURL = WebURLBase + "/" + SearchBoard + "/" + WebURLEnd
    print(WebURL)
    
    #Get the index page 
    soup = get_web_page(WebURL)

    #Get the "上頁" path
    for entry in soup.select('.action-bar'):
        for linktag in entry.findAll('a',href=True):
            if UpPageKW in linktag.text:
                if linktag.get('href').startswith(PttLinkTag):
                    UpPage = PttURL+linktag.get('href')
                    print("UpPage: "+UpPage)
    
    UpPageIndex = int(UpPage[UpPage.index('index')+5:UpPage.index('.html')])
    print("UpPageIndex:",UpPageIndex)
    print("----------------------------------------------------------")

    #Get the key word result in PageRange
    for x in range(SearchPageRange-1,-1,-1):
        print("######################Page: ", x+1, " ######################")
        WebURL = WebURLBase + "/" + SearchBoard + "/index" + str(UpPageIndex-x) + ".html"
        soup = get_web_page(WebURL)
        search_result(soup, SearchKW, PttURL, PttLinkTag)

    #Get the key word result in index page
    print("######################Top Page######################")
    search_result(soup, SearchKW, PttURL, PttLinkTag)



