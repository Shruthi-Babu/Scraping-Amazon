# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url2='https://www.amazon.in/s/ref=sr_pg_5?fst=as%3Aon&rh=k%3Asmart+phones%2Cn%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031&page=5&keywords=smart+phones&ie=UTF8&qid=1522253014'
page=requests.get(url2)
soup=BeautifulSoup(page.content,'html.parser')
possible_links = soup.find_all('a', class_='s-access-detail-page')

for link in possible_links:
    if link.has_attr('href'):
        j = link.attrs['href']
        soup2= BeautifulSoup(requests.get(j).text,'lxml')
        for m in soup2.find_all('td',class_='value'):
            print m.text
        

