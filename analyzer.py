import pandas as pd
import matplotlib.pyplot as plt

# 📊 Data Analyzer for Book Statistics and Visualizations

def save_data(data, loaded_data: pd.DataFrame) :
    """💾 Save scraped book data to CSV file"""
    books_titles = []
    books_prices = []
    books_ratings = []

    # Avoid Data Which Allready Saved & Maintain Which Is New
    for book in data :
        res = book["title"] in loaded_data["Title"].values
        if (not res) :
            books_titles.append((book["title"]))
            books_prices.append((book["price"]))
            books_ratings.append(int(book["rating"]))

    books_info = pd.DataFrame({"Title": books_titles, "Price" : books_prices, "Rating": books_ratings})
    
    # Marge Two DataFrame
    if (not loaded_data.empty) :
        books_info = pd.concat([books_info, loaded_data], ignore_index=True) 
    
    print(books_info)
    books_info.to_csv("data/books.csv", sep ='\t', index=False)

def load_data() :
    """📂 Load book data from CSV file"""
    try:
        df = pd.read_csv("data/books.csv", sep= '\t')
        return df
    except:
        return pd.DataFrame([])

def show_summary() :
    """📋 Display summary statistics of book data"""
    data:pd.DataFrame = load_data()
    average = 0
    most_expensive = cheapest = None

    if (data.empty) :
        print("⚠️ No data found to summarize")
        return

    for row in data.iterrows() :
        row_l = list(row)[1]

        book_price = float(row_l["Price"])
        average += book_price
        if (most_expensive is None or float(most_expensive["Price"]) < book_price):
            most_expensive = {
                "Title" : row_l["Title"],
                "Price": row_l["Price"],
                "Rating" : row_l["Rating"]
            }
        
        if (cheapest is None or float(cheapest["Price"]) > book_price):
            cheapest = {
                "Title" : row_l["Title"],
                "Price": row_l["Price"],
                "Rating" : row_l["Rating"]
            }

    print(f"💰 Most Expensive Book : \n\t{most_expensive}")
    print(f"💵 The Cheapest Book : \n\t{cheapest}")
    print(f"📊 Average Price : {data["Price"].mean():.2f}")
    print(f"💵 Total Price : {average}")
    print(f"📚 Total Books : {data.size / len(data.columns)}")


def show_chart() :
    """📈 Display pie chart of book rating distribution"""
    data:pd.DataFrame = load_data()

    if (data.empty) :
        print("⚠️ No data found to draw chart")
        return

    rates = ["One", "Two", "Three", "Four", "Five"]
    values = [0] * 5

    for row in data.iterrows():
        row_l = list(row)[1]
        values[row_l["Rating"]-1] += 1

    plt.pie(values, labels=rates, autopct="%1.1f%%", explode=(0.1, 0, 0, 0, 0), shadow=True)
    plt.title("📊 Book Rating Distribution")
    plt.show()


def filter_books(max_price = None, min_rating = None) :
    """🔍 Filter books by price and/or rating"""
    data:pd.DataFrame = load_data()

    if (data.empty) :
        print("⚠️ No data found to filter")
        return

    result = pd.DataFrame([])
    if (max_price and min_rating) :
        result = data[(data["Price"] <= max_price) & (data["Rating"] >= min_rating)]
    elif (max_price) :
        result = pd.concat([result, data[data["Price"] <= max_price]], ignore_index=True)
    elif (min_rating) :
        result = pd.concat([result, data[data["Rating"] >= min_rating]], ignore_index=True)

    if (result.empty) :
        print("❌ No books found matching your criteria.")
    else : 
        print("✅ Filter Results:")
        print(result + '\n')
        print("==================")
