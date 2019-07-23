#Yusuf Cattaneo
#G Number: G00983582

from bs4 import BeautifulSoup
import csv
import requests
#Need to put the r below because its a raw file path
new_file = r'C:\Users\ycattaneo\AppData\Local\Programs\Python\Python37-32\Scripts\output.csv'
page_link = 'https://repo.vse.gmu.edu/ait/AIT580/580books.html'
page_response = requests.get(page_link, timeout=5)
page_content = BeautifulSoup(page_response.content, "html.parser")
table = page_content.find('table')
for i,tr in enumerate(table.findAll('tr')):
    row = []
    for td in tr.findAll('td'):
        row.append(td.text)
    if i == 0: # write header
        with open(new_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, row)
            writer.writeheader() # header
    else:
        with open(new_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)
#Part 2
#Prepping the data
import pandas as pd
df = pd.read_csv(r'C:\Users\ycattaneo\AppData\Local\Programs\Python\Python37-32\Scripts\output.csv')
df = pd.DataFrame(df)
print (df)
#Below allows you to view all column names
for col in df.columns: 
    print(col) 
df.columns.str.strip()
list(df)
#Renaming column names to remove \n
df.rename(columns={'Title\n':'Title',
                          'Author(S)\n':'Author',
                          'Publisher\n':'Publisher', 
                          'PubDate\n': 'PubDate'},
                 inplace=True)
#a) Print the frequency count for publishers (that is, how many books for each publisher).
afreq = df['Publisher'].value_counts()
print(afreq)
#b) Visualize the output of (a) using a chart of your own choice.
ax = afreq.plot.bar(x='Publisher', y='val', rot=0)
#c) Print the frequency count for year of publication.
print(df['PubDate'].head(15))
#Just extracting the year from PubDate
import datetime as dt
#Creates a new column Year and puts it in mm/dd/yyy format
df['Year'] = pd.to_datetime(df['PubDate'])
type(df['PubDate'])
#Converts mm/dd/yyy to just yyyy
df['Year']=pd.to_datetime(df['Year'], format='%mm/%dd/%YYYY').dt.year
print(df['Year'].head(15))
cfreq = df['Year'].value_counts()
print(cfreq)
#d) Visualize the output of (b) using a chart of your own choice.
import matplotlib.pyplot as plt
#Can use either plot.box/pie/bar
ad = cfreq.plot.pie(x='Year', y='Count', rot=0)



