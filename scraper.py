import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

def scrape_books(page = 1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    books = []

    soup = BeautifulSoup(response.text, "html.parser")
    
    boxs = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for box in boxs:
        title = box.find("h3").find("a")["title"]
        price = box.find('p', class_="price_color").text
        rating = box.find('p', class_="star-rating")["class"][1]
        books.append({
            "title": title,
            "price": price,
            "rating": rating
        })

    return books



scraped_books = scrape_books()
print(scraped_books)