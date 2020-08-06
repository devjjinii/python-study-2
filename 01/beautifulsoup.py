'''
pip install (https://pypi.org/)
https://pypi.org/project/beautifulsoup4/ (pip install beautifulsoup4)
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

'''
pip list
pip show beautifulsoup4
pip install --upgrade beautifulsoup4
pip uninstall beautifulsoup4

list of python builtins : 내장함수
list of python modules : 외장함수
'''
