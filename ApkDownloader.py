import requests
from bs4 import BeautifulSoup
import urllib.request
import bs4.builder._html5lib

       
def downLoader(link):
    res = requests.get(link)
    res.raise_for_status()  
    s = 'F:\\baiduHotAPKS\\' + link.split('/')[-1]
    print(s)
    playFile = open(s, 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()

resp = urllib.request.urlopen('http://as.baidu.com/a/rank?cid=100&s=1&pn=7')
html_doc = resp.read()
soup = BeautifulSoup(html_doc, 'html5lib')
i = 0
for link in soup.find_all('a'):
    href = link.get('href')
    if href == '###':
        i = i + 1
        print(str(i) + " " + link.get('data-download_url'))
        downLoader(link.get('data-download_url'))

    
    
