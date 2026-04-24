import pandas as pd

def save_data(data, loaded_data) :

    books_titles = [book["title"] for book in data]
    books_prices = [book["price"] for book in data]
    books_ratings = [book["rating"] for book in data]

    books_info = pd.DataFrame({"Title": books_titles, "Price" : books_prices, "Rating": books_ratings})
    if (not loaded_data.empty) :
        books_info = pd.concat([books_info, loaded_data], ignore_index=True)
    
    print(books_info)
    books_info.to_csv("data/books.csv", sep ='\t', index=False)

def load_data() :
    try:
        df = pd.read_csv("data/books.csv", sep= '\t')
        return df
    except:
        return pd.DataFrame([])