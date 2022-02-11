
import requests
import bs4
import re

res = requests.get('https://kanobu.ru/videogames/')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
soup = str(soup)

to_find =  re.compile(r'\>\{.*?(\}\<\/script\>)')

data = to_find.search(soup)

print(data.group(0))