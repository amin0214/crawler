import requests
from bs4 import BeautifulSoup as bs

url = "https://water.taiwanstat.com/"
rsp = requests.get(url)

# 抓取回傳的狀態碼，200表成功
if rsp.status_code != 200:
    print(f'抓取網頁發生錯誤，代碼:{rsp.status_code}')
    quit() # 結束程式

soup = bs(rsp.text, 'html.parser') #可用html5lib，但要先pip安裝
print(soup.prettify())  # prettify()用來把 html 程式變漂亮