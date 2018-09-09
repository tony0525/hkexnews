import csv
import requests
import itertools
from bs4 import BeautifulSoup

r = requests.get('http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY_C.HTM')
soup = BeautifulSoup(r.content)

alist = []
blist = []
clist = []

datelist = []
timelist = []
numberlist = []

date2list = []
time2list = []
number2list = []

finaldatelist = []
finaltimelist = []
finalnumberlist = []

d_tags = soup.find_all('tr', {'class': 'row0'})
e_tags = soup.find_all('tr', {'class': 'row1'})

a_tags = soup.find_all('nobr')
b_tags = soup.find_all('div', {'id': 'hdLine'})
c_tags = soup.find_all('a', {'class': 'news'})

for row1 in a_tags:
	alist.append(row1.text)

	
for row2 in b_tags:
	blist.append(row2.text)

	
for row3 in c_tags:
	clist.append(row3.text)

	
for row in d_tags:
	date = row.text[:10]
	datelist.append(date)
	time = row.text[10:15]
	timelist.append(time)
	number = row.text[15:20]
	numberlist.append(number)
	
for row in e_tags:
	date = row.text[:10]
	date2list.append(date)
	time = row.text[10:15]
	time2list.append(time)
	number = row.text[15:20]
	number2list.append(number)	
	
finaldatelist = list(itertools.chain.from_iterable(zip(datelist,date2list)))
finaltimelist = list(itertools.chain.from_iterable(zip(timelist,time2list)))
finalnumberlist = list(itertools.chain.from_iterable(zip(numberlist,number2list)))

	
with open('hkex_news.csv', 'w', newline='' , encoding = 'utf-8-sig') as output:
	writer = csv.writer(output)
	writer.writerow(["發放日期", "發放時間", "代號", "股份名稱", "文件類型", "詳細資料"])
	rows = zip(finaldatelist,finaltimelist,finalnumberlist,alist,blist,clist)
	writer2 = csv.writer(output)
	
	for roww in rows:
		writer.writerow(roww)