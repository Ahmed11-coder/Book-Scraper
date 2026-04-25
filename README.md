# 📚 Book Scraper & Data Analyzer 📊

A powerful web scraping and data analysis tool for collecting book information from [Books to Scrape](https://books.toscrape.com/) and analyzing the data with visualizations.

## ✨ Features

- 🌐 **Web Scraping**: Scrape book data including title, price, and rating from multiple pages
- 💾 **Data Persistence**: Save scraped data to CSV format for future analysis
- 📊 **Data Analysis**: Generate summaries with statistics like average price, most/least expensive books
- 📈 **Visualizations**: Create pie charts showing book rating distributions
- 🔍 **Filtering**: Filter books by maximum price, minimum rating, or both
- 🔄 **Incremental Updates**: Avoid duplicates when scraping new data

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Book-Scraper.git
cd Book-Scraper
```

2. Install required dependencies:
```bash
pip install requests beautifulsoup4 pandas matplotlib
```

3. Create the data directory:
```bash
mkdir data
```

## 🚀 Usage

Run the main script:
```bash
python main.py
```

### Menu Options

1. **Scrape New Data** 📥
   - Enter a page range to scrape books from
   - Data is automatically saved to `data/books.csv`

2. **Show Summary** 📋
   - Displays statistics:
     - Most expensive book
     - Cheapest book
     - Average price
     - Total price
     - Total number of books

3. **Show Chart** 📊
   - Displays a pie chart showing the distribution of book ratings (1-5 stars)

4. **Filter Books** 🔍
   - Filter by maximum price
   - Filter by minimum rating
   - Filter by both criteria

5. **Exit** 👋
   - Exit the application

## 📁 Project Structure

```
Book-Scraper/
├── main.py          # Main CLI interface
├── scraper.py       # Web scraping functionality
├── analyzer.py      # Data analysis and visualization
├── data/
│   └── books.csv    # Scraped book data storage
└── README.md        # Project documentation
```

## 🔧 Dependencies

- `requests` - HTTP library for web scraping
- `beautifulsoup4` - HTML parsing
- `pandas` - Data manipulation and analysis
- `matplotlib` - Data visualization

## 📝 Example Workflow

1. Start the application: `python main.py`
2. Select option `1` to scrape books (e.g., pages 1-5)
3. Select option `2` to view a summary of your data
4. Select option `3` to visualize rating distributions
5. Select option `4` to find books under £20 with 4+ star ratings

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by [Your Name]

---

Made with ❤️ and Python