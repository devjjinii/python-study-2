from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

# https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC
baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)

# print(url)
driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source # 열린페이지소스
soup = BeautifulSoup(html)

r = soup.select('.r')
for i in r:
    print(i.select_one('.LC20lb.DKV0Md').text) 
    # list 여서 one
    # print(i.select_one('.iUh30.bc').text)
    print(i.a.attrs['href'])
    print()

driver.close()