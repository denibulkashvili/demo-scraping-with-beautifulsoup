from bs4 import BeautifulSoup
import requests

source = requests.get('https://codepen.io/').text
soup = BeautifulSoup(source, 'lxml')

pen = soup.find('div', class_="single-pen")
 

print(title)
