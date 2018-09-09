from bs4 import BeautifulSoup
import requests
import csv
import datetime


indeed_home = "https://th.indeed.com/"
search_query = "jobs?q=Python+Developer&sort=date"
source = requests.get(indeed_home+search_query).text
soup = BeautifulSoup(source, 'lxml')

now =  datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
fname = date+".csv"

csv_file = open(fname, 'w', encoding="utf-8")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'company', 'location', 'summary', 'link'])


jobs = soup.find_all('div', class_="result") 

for job in jobs:
    title = job.h2.a.text
    company = job.div.span.text.lstrip()
    location = job.find('span', class_="location").text
    summary = job.find('span', class_="summary").text.lstrip()
    link = indeed_home + job.h2.a['href']

    csv_writer.writerow([title, company, location, summary, link])

csv_file.close()
