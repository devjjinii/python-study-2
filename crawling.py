import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusUrl =  input('검색어를 입력하세요 : ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)  #인코딩문제

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)
title = soup.find_all(class_='sh_blog_title')

# print(len(title))
for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()