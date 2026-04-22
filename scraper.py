import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def scrape_books(page = 1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)


    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())