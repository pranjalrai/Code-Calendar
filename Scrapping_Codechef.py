#This snippet of code collects details of upcoming and present contests from Codechef and stores it into a file named 'codechef.txt'


from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd


f = open('codechef.txt', 'w')


source = requests.get('http://codechef.com/contests').text

soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('table',class_='dataTable')[0] 
    
row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        if column_marker is 1 :
            s = str(column.find('a')).split('"')
            r='codechef.com'
            link = r+s[1]
            f.write(link)
            f.write("\n")
        f.write(column.get_text())
        f.write("\n")

        column_marker += 1
    f.write("\n")

#new_table


soup = BeautifulSoup(source, 'lxml')
table = soup.find_all('table',class_='dataTable')[1]     


    
row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        if column_marker is 1 :
            s = str(column.find('a')).split('"')
            r='codechef.com'
            link = r+s[1]
            f.write(link)
            f.write("\n")
        contestname=column.get_text()
        f.write(contestname)
        f.write("\n")

        column_marker += 1
    f.write("\n")



f.close()
















