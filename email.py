import requests
from bs4 import BeautifulSoup as bs

url = 'https://temp-mail.org/en/'

x = requests.get(url)

source = bs(url.content, 'html')
print(source.title)