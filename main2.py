'''
Project:
URL Link: https://sofifa.com/players

#1st Page
https://sofifa.com/players or https://sofifa.com/players?offset=0
#2nd Page
https://sofifa.com/players?offset=60
#3rd Page
https://sofifa.com/players?offset=120
.
.
.
#10th Page
https://sofifa.com/players?offset=540
'''

arr= [0, 60, 120, 180, 240, 300, 360, 420, 480, 540]

for i in arr:
  url=(f'https://sofifa.com/players?offset={i}')
  print(url)
  
#Parameters
NAME= []
AGE= []
OVA= []
POT= []
TEAM_NA= []
CONTRACT= []
VALUE(M)= []
WAGE(K)= []
TOTAL_STAT= []

for i in arr:
  url=(f'https://sofifa.com/players?offset={i}')
  resp= requests.get(url)
  soup= BeautifulSoup(resp.content, 'lxml')

for name in _____:
  NAME.append(name)
#Web Scraping

import pandas as pd
df= pd.DataFrame({"Name": NAME,
                  "Age": AGE,
                  "Ova": OVA,
                  "Pot": POT,
                  "Team":TEAM_NA,
                  "Contract":CONTRACT,
                  "Value(M)": VALUE,
                  "Wage(K)":WAGE,
                  "Total":TOTAL_STAT})
