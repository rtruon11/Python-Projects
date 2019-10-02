from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
page = Request(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print(name)
