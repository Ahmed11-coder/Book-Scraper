import requests
import re
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def scrape_books(page = 1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    if (response.status_code == 404) : raise ValueError(f"404 Page {page} Not Found")
    books = []

    soup = BeautifulSoup(response.text, "html.parser")

    boxs = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for box in boxs:
        title = box.find("h3").find("a")["title"]
        price = box.find('p', class_="price_color").text
        rating = box.find('p', class_="star-rating")["class"][1]
        books.append({
            "title": title,
            "price": re.findall("\d+.?\d+", price)[0],
            "rating": rating == "One" and 1 or rating == "Two" and 2 or rating == "Three" and 3 or rating == "Four" and 4 or rating == "Five" and 5
        })

    return books

def scrape_in_range(start_page, end_page):
    all_books = []
    for page in range(start_page, end_page+1):
        books = scrape_books(page)
        all_books.extend(books)
    return all_books