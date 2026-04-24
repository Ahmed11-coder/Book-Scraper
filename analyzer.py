import pandas as pd
import matplotlib.pyplot as plt

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

def show_summary() :
    data = load_data()
    average = 0
    most_expensive = cheapest = None

    for row in data.iterrows() :
        row_l = list(row)[1]

        book_price = float(row_l["Price"][2:])
        average += book_price
        if (most_expensive is None or float(most_expensive["Price"][2:]) < book_price):
            most_expensive = {
                "Title" : row_l["Title"],
                "Price": row_l["Price"],
                "Rating" : row_l["Rating"]
            }
        
        if (cheapest is None or float(cheapest["Price"][2:]) > book_price):
            cheapest = {
                "Title" : row_l["Title"],
                "Price": row_l["Price"],
                "Rating" : row_l["Rating"]
            }

    print(f"Most Expensive Book : \n\t{most_expensive}")
    print(f"The Cheapest Book : \n\t{cheapest}")
    print(f"Average Price : {average/(data.size / len(data.columns))}")
    print(f"Total Price : {average}")
    print(f"Size : {data.size / len(data.columns)}")

def show_chart() :
    data = load_data()
    rates = ["One", "Two", "Three", "Four", "Five"]
    values = [0] * 5

    for row in data.iterrows():
        row_l = list(row)[1]
        values[row_l["Rating"]-1] += 1

    plt.pie(values, labels=rates, autopct="%1.1f%%", explode=(0.1, 0, 0, 0, 0), shadow=True)
    plt.title("Books Rates")
    plt.show()