import analyzer as ana
from scraper import scrape_in_range


print("======== Scraping Books =======")
print("Menu:")
print("1. Scrape New Data")
print("2. Show Summary")
print("3. Show Chart")
print("4. Filter Books")
print("5. Exit")

loaded_data = ana.load_data()

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        start_page = int(input("Enter the start page: "))
        end_page = int(input("Enter the end page: "))

        scraped_books = scrape_in_range(start_page, end_page)
        ana.save_data(scraped_books, loaded_data)
    elif choice == 2:
        ana.show_summary()
    
    elif choice == 3:
        ana.show_chart()

    elif choice >= 5:
        print("Exiting...")
        break
    
    else :
        print("Option not implemented yet.")