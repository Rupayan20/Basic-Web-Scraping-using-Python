#import libraries
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

#import url
url='https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'

resp= requests.get(url)
resp.status_code
soup= BeautifulSoup(resp.content, 'lxml')
print(soup)

arr= []
for i in soup.findAll('td'):
  arr.append(str(i))
  print(arr)

#we need to do scrapthe datafrom our raw data
re.sub('^<td>.*">|</a></td>|</a></i></td>|</b>|<td>|</td>|\n','',arr[0])
for i in arr:
  print(re.sub('^<td>.*">|</a></td>|</a></i></td>|</b>|<td>|</td>|\n','',(i)))
