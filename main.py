import analyzer as ana
from scraper import scrape_in_range


print("📚 ===== Scraping Books ===== 📚")
print("📋 Menu:")
print("1. Scrape New Data 📥")
print("2. Show Summary 📊")
print("3. Show Chart 📈")
print("4. Filter Books 🔍")
print("5. Exit 👋")


while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("⚠️ Please enter a number.\n")
            continue

        if choice == 1:
            while True:
                try:
                    start_page = int(input("Enter the start page: "))
                    end_page = int(input("Enter the end page: "))
                    break
                except ValueError:
                    print("⚠️ Please enter a valid integer value\n")

            scraped_books = scrape_in_range(start_page, end_page)
            loaded_data = ana.load_data()
            ana.save_data(scraped_books, loaded_data)
        elif choice == 2:
            ana.show_summary()
        
        elif choice == 3:
            ana.show_chart()

        elif choice == 4:
            while True:
                try:
                    print("🔍 Filter Options:")
                    print("\t1. By Max Price 💰")
                    print("\t2. By Min Rating ⭐")
                    print("\t3. Both 🎯")
                    filter_choice = int(input("Choose: "))
                    if (filter_choice > 3) : raise ValueError
                    break
                except ValueError:
                    print("⚠️ Please enter a valid value (1-3)\n")

            if (filter_choice == 1) :
                max_price = float(input("Enter Max Price: "))
                ana.filter_books(max_price)

            elif (filter_choice == 2) :
                min_rating = int(input("Enter Min Rate (1-5): "))
                ana.filter_books(None, min_rating)

            elif (filter_choice == 3):
                max_price = float(input("Enter Max Price: "))
                min_rating = int(input("Enter Min Rate (1-5): "))
                ana.filter_books(max_price, min_rating)

        elif choice >= 5:
            print("👋 Exiting...")
            break
        
        else :
            print("❌ Option not implemented yet.")