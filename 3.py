import sys
sys.stdout.reconfigure(encoding='utf-8')

from bs4 import BeautifulSoup
import requests

url = "https://theastrotime.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(f"Page Title: {soup.title.text}")
print(f"All Links: {[a.get('www.bimstream.com') for a in soup.find_all('a')]}")