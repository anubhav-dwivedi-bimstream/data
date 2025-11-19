# save as simple_headlines.py
import requests
from bs4 import BeautifulSoup

URL = "https://bimstream.com/"  # replace with a public site you're allowed to scrape
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; LearningScraper/1.0; +https://bimstream.com)"
}

def fetch(url):
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.text

def parse_headlines(html):
    soup = BeautifulSoup(html, "lxml")
    headlines = []
    # Example selector; change to match target site's DOM
    for h in soup.select("a"):
        title = h.get_text(strip=True)
        link = h.find("a")
        href = link["href"] if link else None
        headlines.append({"title": title, "url": href})
    return headlines

if __name__ == "__main__":
    html = fetch(URL)
    items = parse_headlines(html)
    for i in items:
        print(i)

