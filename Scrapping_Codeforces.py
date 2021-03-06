#This snippet of code collects details of upcoming and present contests from Codeforces and stores it into a file named 'codeforces.txt'
#on local machine.



from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd


f = open('codeforces.txt', 'w')


source = requests.get('http://codeforces.com/contests').text

soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('table')[0]

    
row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        if (column_marker!=0 and column_marker!=2):
            column_marker+=1
            continue
        
        f.write(column.get_text())
        f.write("\n")

        column_marker += 1


f.close()















