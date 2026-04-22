import pandas as pd

def save_data(data) :

    books_titles = [book["title"] for book in data]
    books_prices = [book["price"] for book in data]
    books_ratings = [book["rating"] for book in data]

    books_info = pd.DataFrame({"Title": books_titles, "Price" : books_prices, "Rating": books_ratings})
    print(books_info)
    books_info.to_csv("data/books.csv", sep ='\t')